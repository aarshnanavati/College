 <form action="<?php $_PHP_SELF ?>" >
  First name:<br>
  <input type="text" name="firstname" value=""><br>
  Last name:<br>
  <input type="text" name="lastname" value=""><br><br>
  <input type="submit" value="Submit" name="Submit">
  <input type="reset">
</form> 

<?php
   if( $_REQUEST["Submit"] ) //$_REQUEST is an associative array that by default contains contents of an $_GET, $_POST, and $_COOKIE.
   {
      echo "Welcome ". $_REQUEST['firstname']. $_REQUEST['lastname'];
      exit();
   }
 
?>
