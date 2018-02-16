
---
#  Professional WordPress
## by Brad Williams
---

 - loc 1045 - The mysql_error() function is a PHP library function that spits out the error generated by the last MySQL function called.

 - loc 1239 - Core files are all files in the wp-admin and wp-includes directories and the majority of the files in the root WordPress directory. The wp-content directory holds all of your custom files, including themes, plugins, and media. This directory contains the code that controls content manipulation and presentation in WordPress.

 - loc 1262 - The most important file in any WordPress installation is the wp-config.php file. This file contains all database connection settings, including the database name, username, and password, to access your MySQL database.

 - loc 1277 - Moving the wp-config.php out of the root WordPress directory is a good security measure, making it nearly impossible to potentially access this file from a web browser.

 - loc 1354 - define( 'WP_SITEURL', 'http://example.com/wordpress' );

 - loc 1356 - The WP_SITEURL option allows you to temporarily change the WordPress site URL. This does not alter the database option value for siteurl, but instead temporarily changes the value.

 - loc 1362 - This is a useful technique if you are building a WordPress website under a temporary development URL, such as new.example.com. You can simply remove these two options when you go

 - loc 1422 - A great debugging option is SAVEQUERIES. Activating this option saves all database queries into a global array that can be displayed on your page.

 - loc 1427 - define( 'SAVEQUERIES', true ); To display the query array in your theme, add the following code to any theme template file to view: if ( current_user_can( 'manage_options' ) ) {   global $wpdb;   print_r( $wpdb->queries );}

 - loc 1448 - define( 'WP_MEMORY_LIMIT', '64M' );

 - loc 1516 - There is a PHP function to view all constants currently set on your installation: print_r( @get_defined_constants() );

 - loc 1519 - To activate SSL on login, add the FORCE_SSL_LOGIN option like so: define( 'FORCE_SSL_LOGIN', true ); You can also force all admin pages to use SSL. This is activated with the FORCE_SSL_ADMIN option, like so: define( 'FORCE_SSL_ADMIN', true );

 - loc 1553 - A great resource for learning about wp-config.php options is the Codex: http://codex.wordpress.org/Editing_wp-config.php

 - loc 1588 - pretty permalinks are controlled by the mod_rewrite Apache module.

 - loc 1673 - php_flag display_startup_errors offphp_flag display_errors offphp_flag html_errors offphp_flag  log_errors onphp_value error_log /public_html/php-errors.log This enables error logging but suppresses any error messages from displaying. Again this is a perfect setup for a production environment because you don’t want errors publicly displayed.

 - loc 1710 - Plugins are stored in the wp-content/plugins directory.

 - loc 1760 - The W3 Total Cache plugin (https://wordpress.org/plugins/w3-total-cache/) creates a /wp-content/cache directory to store all of the cached pages created for your website. A cached page is simply a fully generated page on your website saved as a static HTML file.

 - loc 1769 - The most popular image gallery plugin, NextGen Gallery (http://wordpress.org/extend/plugins/nextgen-gallery/), creates a /wp-content/gallery directory to store all of the images uploaded to your NextGen image galleries. Each gallery created is a subdirectory under /gallery.

 - loc 1985 - You set your PHP error level in the php.ini file.

 - loc 1986 - Set your error reporting directive to be E_ALL and E_STRICT,

 - loc 2016 - Essentially, he changes the wp-config.php file to look for an overriding set of credentials that exist on his development machine only. He then ignores this wp-config-local.php file in his source code control so that each developer can have his or her own controlled local credentials and so that this file never makes it to production.

 - loc 2134 - For this process you use the wp-DBManager plugin by Lester Chan available online at https://wordpress.org/plugins/wp-dbmanager/. This plugin allows you to make database backups and also perform SQL queries on the data.

 - loc 2226 - PHPDoc is a standardized method of describing a function’s usage in PHP comment form.

 - loc 2358 - The pluggable functions file lets you override certain core functions of WordPress.

 - loc 2480 - The official Function Reference is located at http://codex.wordpress.org/Function_Reference

 - loc 2528 - An example core WordPress shortcode is [gallery]. Adding [gallery] to your post automatically displays all images uploaded to that post in a gallery style.

 - loc 2611 - The biggest benefit to the Code Reference over the Codex is accuracy. The Code Reference is automatically generated from the WordPress core files. This ensures all content in the Code Reference is completely accurate and always up to date with the latest version of WordPress.

 - loc 2661 - The Loop refers to how WordPress determines what content (posts, pages, or custom content) to display on a page you are visiting.

 - loc 2661 - The Loop refers to how WordPress determines what content (posts, pages, or custom content) to display on a page you are visiting. The Loop can display a single piece of content or a group of posts and pages that are selected and then displayed by looping through the content; thus, it’s called the Loop.

 - loc 2741 - If you want to explore the core for the gory details of SQL generation, most of the query-to-request parsing is done in wp-includes/query.php, and the bulk of the JOIN work is set up in wp-includes/taxonomy.php.

 - loc 2751 - content, WordPress will insert a LIKE modifier into the WHERE clause that contains the post name. For example, if a user supplies the URL http://example.com/2015/lecter, but you have no posts with the title “Lecter,” the LIKE clause will match any posts that start with “Lecter,” such as “Lecter Fish IPA Review.”

 - loc 2751 - if an attempt to load a page by name fails to return any content, WordPress will insert a LIKE modifier into the WHERE clause that contains the post name. For example, if a user supplies the URL http://example.com/2015/lecter, but you have no posts with the title “Lecter,” the LIKE clause will match any posts that start with “Lecter,” such as “Lecter Fish IPA Review.”

 - loc 2752 - if a user supplies the URL http://example.com/2015/lecter, but you have no posts with the title “Lecter,” the LIKE clause will match any posts that start with “Lecter,” such as “Lecter Fish IPA Review.”

 - loc 2786 - Keep in mind that a Loop is effectively a database query to select content and then an iteration over the selection to display

 - loc 2824 - Calling the_post() in turn calls the setup_postdata() function to set up the per-post metadata such as the author and tags of the content you are displaying

 - loc 2827 - Specifically calling the_post() has the side effect of setting up the global $post variable used by most of the template tags described later on, and then advances to the next post in the list.

 - loc 2869 - PHP functions used in your WordPress theme templates to display Loop content are called template tags.

 - loc 2929 - You can also use the Codex for a detailed description of the template tag you are working with, in this case http://codex.wordpress.org/Template_Tags/the_title

 - loc 3100 - The pre_get_posts hook accepts the global WordPress query by reference, which enables you to modify the query variables prior to having the query run.

 - loc 3131 - The query_posts() function is used to easily modify the content returned for the default WordPress Loop. Specifically, you can modify the content returned in $wp_query after the default database query has executed, fine-tune the query parameters, and re-execute the query using query_posts().
