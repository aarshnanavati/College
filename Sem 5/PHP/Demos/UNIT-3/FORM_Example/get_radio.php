<?php
if(isset($_GET["firstname"])&&isset($_GET["lastname"])&&isset($_GET["gender"]))
{
echo "Welcome " . $_GET["firstname"]." ".$_GET["lastname"]." ".$_GET["gender"];
}
?>
<html>
<head>
<title>Registration Form</title>
</head>
<body>
<h2>Registration Form</h2>
<form action="<?php $_PHP_SELF ?>" method="GET" > 
First name:
<input type="text" name="firstname"><br> 
Last name: 
<input type="text" name="lastname"> <br> 
Gender:
<input type="radio" name="gender" value="female">Female
<input type="radio" name="gender" value="male">Male
<input type="radio" name="gender" value="other">Other
<input type="submit" value="Submit"> 
</form> </body> 
</html>

