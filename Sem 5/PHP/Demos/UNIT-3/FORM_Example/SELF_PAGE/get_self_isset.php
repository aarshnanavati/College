<?php
if(!empty($_GET["firstname"])&& !empty($_GET["lastname"]))
{
echo "Welcome " . $_GET["firstname"]." ".$_GET["lastname"];
//var_dump(!empty($_GET["firstname"]));
}

/*
if(isset($_GET["firstname"])&& isset($_GET["lastname"]))
{
echo "Welcome " . $_GET["firstname"]." ".$_GET["lastname"];
var_dump(isset($_GET["firstname"]));
}
*/
?> 
<html>

<head>

<title>Registration Form</title>


</head>

<body>

<h2>Registration Form</h2>

<form action="<?php $_PHP_SELF ?>" method="GET" > 
First name:

<input type="text" name="firstname"><br> Last name: 

<input type="text" name="lastname"> <br> 

<!--<input type="hidden" name="form_submitted" value="1"/> -->

<input type="submit" value="Submit"> 

</form> 

</body> 

</html>

