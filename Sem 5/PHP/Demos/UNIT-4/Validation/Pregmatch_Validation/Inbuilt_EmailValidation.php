

<html>

<body>
<link rel="stylesheet" type="text/css" href="style.css">
<?php

$email = "def@gmail.com";

if (filter_var($email, FILTER_VALIDATE_EMAIL)) //This is a PHP built-in function that checks whether the value of $email is a valid email address format.
{
    echo("$email is a valid email address");
 
} else {
  echo("$email is not a valid email address");
}

echo "<h1> sdf </h1>";
?> 
</body>
</html>
