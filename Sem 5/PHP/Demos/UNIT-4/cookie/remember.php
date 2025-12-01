<?php
if(!empty($_POST["remember"])) 
{
	setcookie ("username",$_POST["username"],time()+ 3600);
	setcookie ("password",$_POST["password"],time()+ 3600);
	echo "Cookies Set Successfuly";
} 
else if(isset($_COOKIE["username"])) 
{
	setcookie("username","");
	setcookie("password","");
	echo "Cookies Deleted";
}
else
	echo "Cookies Not set";
 
?>
 

