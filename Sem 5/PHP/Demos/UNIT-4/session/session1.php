<?php
   session_start(); 
//This function starts a new session or resumes the existing one. Without this line, you cannot use the $_SESSION superglobal.
   
   if( isset( $_SESSION['counter'] ) ) {
      $_SESSION['counter'] += 1;
      
   }else {
      $_SESSION['counter'] = 1;
   }
//This checks if the session variable counter is already set. If yes → it increases its value by 1. If no → it initializes counter with value 1.
	
  //echo "You have visited this page " . $_SESSION['counter'] . " times in this session.";
   $msg = "You have visited this page ".  $_SESSION['counter'];
   $msg .= "in this session.";
   //Prepares a message string showing how many times you’ve opened/reloaded this page during the session.
?>

<html>
   
   <head>
      <title>Setting up a PHP session</title>
   </head>
   
   <body>
      <?php  echo ( $msg ); ?>
   </body>
   
</html>

<!--
<?php
   unset($_SESSION['counter']);
   //If you uncomment this code, it will remove the counter variable from the session (like a reset).
//On the next page load, $_SESSION['counter'] will no longer exist, so the script will reinitialize it to 1 again.
?>
-->
