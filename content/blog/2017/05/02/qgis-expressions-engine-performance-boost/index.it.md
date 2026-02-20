---
title: 'QGIS Expressions Engine: Performance boost – OPENGIS.ch'
date: 2017-05-02
slug: "qgis-expressions-engine-performance-boost"
url: "/it/2017/05/02/qgis-expressions-engine-performance-boost/"
source: "www.opengis.ch/it/2017/05/02/qgis-expressions-engine-performance-boost/index.html"
---
Expressions in QGIS are more and more widely used for all kinds of purposes.
For example the recently introduced [geometry generators](</2015/12/10/geometry-generator-symbology/index.html>) allow drawing awesome effects with modified feature geometries on the fly.
The last days at the QGIS developer meeting 2017, I spent some time looking into and improving the performance for expressions. This was something that was on my todo list for a while but I never got around to working on it.
Short story:
  - **Some expressions used as part of the[2.5D rendering](</2015/11/02/qgis-crowdfunding-2-5d-rendering/index.html>) became almost 50% faster**


  - **Overall, 2.5D rendering experiences a performance improvement of 30%**


Read on if you are interested in what we have done and to get some insights into the internal handling of the expression engine.
The complexity will gradually be increased throughout the article.
# Preparing expressions
Since a long time, QgsExpression has a method prepare() . This method should be called whenever an expression is evaluated for a series of features once just before. The easiest example for this is the field calculator:
  1. Create an expression
  2. Prepare the expression
  3. Loop over all the features in the attribute table


Historically, this method has resolved the attribute index in a layer. If a layer has the attributes “id” , “name” and “height” and the expression is “name” || ‘: ‘ || “height” , this would just convert it to column(0) || ‘: ‘ || column(2) . Accessing attributes by index is generally a bit faster than by name, and the index is guaranteed to be static throughout a single request, so it’s an easy win.
# Static nodes
The first thing that happens to an expression in it’s lifetime is, it’s translated from text to a tree of nodes.
A simple example 3 * 5
  - NodeBinaryOperator (operator: *) 
    - left: NodeLiteral( 3 )
    - right: NodeLiteral( 5 )


It’s trivial to see, that we do not need to calculate this everytime for each feature since there are no fields or other magic ingredients involved, it’s always 15: it’s static.
# Precalculating and caching
If we check if an expression only consists of static nodes, we can just precalculate it once and then reuse this value. This also works for partial expressions, let’s say 1 + 2 + “three” can always be simplified to 3 + “three” .  
We just have to find out for every node, if it’s static and then scan for nodes that are only made up of static descendants themselves. The only thing that is not static are the attributes (so NodeColumnRef), right?  
**Performance win number 1: precalculate and cache static values.**
# Functions
In a first step, each function was tagged as non-static and is therefore expected to return a new value for each iteration. This approach is safe, but you guess it, there is plenty of room for improvements.  
Within the 2.5D renderer for example, the following is used (simplified here):
    
    translate( $geometry, cos( radians ( 70 ) ) * 10, sin( radians( 70 ) ) * 10 )
This expression will translate (displace) the footprint of a building by 10 meters with an angle of 70 degrees (that’s where the roof of a large building would be painted).  
The whole part cos(radians(70)) can be simplified to 0.34202 . Of course we could have directly entered this value on the user side, but it’s much more readable and maintainable if we put the calculation there and let the computer do the hard work.  
On the other hand, the outer block translate( $geometry, [x], [y] ) cannot be pre-calculated. It depends on the footprint of the building, so there’s nothing that could be done there.  
Conclusion: a function will return a static value unless one of its parameters is non-static. cos and sin are static because their content is static, translate not, because there’s also the $geometry .  
**Performance win number 2: precalculate and cache functions when they only have static parameters.**
# Dynamic functions
Meet the rand() function. It will always return a different value although it has no non-static parameters. It will just return a new value every time and we do not want it to be cached.  
The conclusion is easy: find all the functions that are not static and tag them as such.  
**Caveat: some functions behave differently.**
# Variables
Next thing in the queue are variables. Variables are an awesomely cool concept that allows to get some properties like the filename of the current layer or project or additional, manually defined project or system-specific values. They are mostly static. Right? Of course not. Some of them get set at rendering time. For example there is a variable @symbol_color , that can be used to get the current symbol color. It allows for creating really cool effects, but we don’t want this value to be cached.  
**Performance win number 3: precalculate and cache variables**  
**Caveat: Only when they really are static**
# The strange kids in the block
And finally there are also the really funky functions. There is for example `eval`, which takes a string as parameter which can be parsed as an expression. Some examples are eval(‘7’) which returns 7 (an integer), eval(‘1>3’) which returns false and eval(“condition”) which reads the content of the field “condition” and treats it as an expression. So a new level enters the equation. Not only the parameter node itself (which is treated as a string) needs to be static, but also the expression that is created from parsing this string.  
**Caveat: when there is a function like eval() or order_parts() that take expression strings as parameters, be extra careful and check if expression string as well as the expression in the string are static.**  
Only pre-calculate if everything is really static. If the expression string is static, but the content is not we can still do something.  
For example when rendering with the 2.5D renderer and setting the building height based on the number of stories (assuming an average room height of 2.7 meters), there would be an expression eval(@25d_height) with the variable @25d_height being set to “stories” * 2.7 . The string is static (@25d_height is a static layer variable). But we can’t precaculate the value (“stories” is not static). However, we can still prevent the expressions engine from reparsing the expression with every iteration and potentially we can even precalculate parts of such an expression. Especially the fact, that the expression does not need to be parsed over and over again results in a big win.  
**Performance win 4: Parse and prepare evaluated expressions if they are static.**
# Conclusion
It was well worth investing the time into improving the more and more used expressions engine. Having a responsive system increases user experience and productivity.  
I only had the chance to work on this thanks to the QGIS developer meeting in Essen. Such events wouldn’t be possible without people and organisations sponsoring the QGIS project and a motivated community. You are all awesome!  
This will be part of QGIS 3.0 which is expected to be released later this year.
# Outlook
While this is a great step forward, it doesn’t stop here.
  - It should be possible to use this new mechanism to put some load from the local QGIS installation to a database server (see our previous project to compile expressions).
  - The whole mechanism only works, if an expression is actually prepared. Unprepared expressions will need to be identified and prepared to make use of this system.


If you would like to support such an initiative, please do not hesitate to contact us. We will love to make QGIS even faster for you!
### _Related_
