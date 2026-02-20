---
title: 'wordpress iphone app with wpml – OPENGIS.ch'
date: 2009-08-07
slug: "wordpress-wpml-iphone-app"
url: "/2009/08/07/wordpress-wpml-iphone-app/"
source: "www.opengis.ch/2009/08/07/wordpress-wpml-iphone-app/index.html"
---
I’ve a client using a wordpress multilingual blog with the wpml plugin ([wpml.org/](<https://wpml.org/>)) and that wants to use the wordpress iphone app ([iphone.wordpress.org](<https://iphone.wordpress.org/>)). The app and the plugin work like a charm. the only problem is that in the app you can’t set the post language, hence you are (well by now were 🙂 ) able to post only using the default language.  
I wrote a small PHP script to put in the root dir of your blog that updates the default language of the blog when called. so basically before using the iphone app you call the script using safari (https://domain.tdl/blog/set_post_lang.php?to=de) and then use the iphone application to post to your blog.  
The script requires minimal configuration, you have to set the blog_id (if you have a single install, 0 should be ok, but you can find this by looking at the wp_options table in the DB) and an array of valid languages. Please note that the script uses no authentication methods, up to you to decide if you want to implement it (very easy actually for example with http_auth or with a key). I didn’t because the script does something very small and irrelevant from the security point of view.  
And here the code, enjoy.
    
    query($query)) && $result->num_rows == 1) {
      while ($row = $result->fetch_assoc()) {
            $value = $row["option_value"];
      }
      /* free result set */
      $result->close();
    }
    else die('Error getting the actual setting');
    /* check if update needed */
    $new_pattern = '"default_language";s:2:"'.$set_to.'"';
    $replace = !preg_match("/$new_pattern/",$value);
    /* change the language then update the DB */
    if($replace){
      $pattern = '/"default_language";s:2:"[a-z]{2}"/';
      $value = preg_replace($pattern , $new_pattern, $value, 1);
      $query = 'UPDATE `'.DB_NAME.'`.`wp_options`
                SET `option_value` = ''.$value.''
                WHERE CONVERT(`wp_options`.`option_name` USING utf8) = "icl_sitepress_settings"
                AND `wp_options`.`blog_id` = '.BLOG_ID.'
                LIMIT 1;';
      if ($result = $mysqli->query($query)) {
        echo 'Default post language is now set to '.strtoupper($set_to);
        }
      else echo 'Problem updating the language, please try again';
    }
    else echo 'Default post language is already set to '.strtoupper($set_to);
    //close DB connection
    $mysqli->close();
    ?>
### _Related_
