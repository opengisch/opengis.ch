---
title: "migrating wordpress from gengo to wpml – OPENGIS.ch"
author: "Marco Bernasocchi"
date: "2009-08-15T15:13:59+02:00"
lastmod: "2020-04-29T16:08:00+02:00"
categories:
  - "Web Development"
tags:
  - "qgis.org"
source: "www.opengis.ch/fr/2009/08/15/migrating-wordpress-from-gengo-to-wpml/index.html"
---

A client of mine used to have a multilingual blog using the Gengo plugin, which I consider by now unfortunatly dead. Fortunately, the guys at https://www.wpml.org did a great job creating a new plugin that works like a charm.  
I did the migration from one to the other and I had no troubles (beside figuring out how to map gengo’s model to wpml). Further down are two SQL statements to check and update the posts language in wpml.  
IMPORTANT: first disable gengo, then install wpml, then choose the default language and create the languages you had in geng. All your post will now be in the default language. you can check this with this SQL statement (for example using phpMyAdmin)
    
    SELECT post.`ID`, post.`post_title`, wpml.`language_code` as wpml_language, gengoLang.`code` as gengo_language
    FROM `wp_posts` post
    LEFT JOIN `wp_icl_translations` wpml on wpml.`element_id` = post.`ID`
    LEFT JOIN `wp_post2lang` gengo on gengo.`post_id` = post.ID
    LEFT JOIN `wp_languages` gengoLang on gengoLang.`language_id` = gengo.`language_id`
    WHERE wpml.`element_type` ='post'
    ORDER BY post.`ID`  DESC;
Then you can update the post language with the following statement:
    
    UPDATE `wp_icl_translations` wpml
    LEFT JOIN `wp_posts` post on wpml.`element_id` = post.`ID`
    LEFT JOIN `wp_post2lang` gengo on gengo.`post_id` = post.ID
    LEFT JOIN `wp_languages` gengoLang on gengoLang.`language_id` = gengo.`language_id`
    set wpml.`language_code` = gengoLang.`code`
    WHERE wpml.`element_type` ='post'
This will update your POSTS only, no category or tags yet. I might look at those as well and I’ll get in touch with wpml to see if they can use my snippets to get out a sort of import tool.  
cheers Marco
### _Related_
