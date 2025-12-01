<?php

echo "Welcome " . $_GET["firstname"]." ".$_GET["lastname"];

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

<input type="submit" value="Submit"> 

</form> 

</body> 

</html>

