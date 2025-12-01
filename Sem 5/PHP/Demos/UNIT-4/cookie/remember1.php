<?php
$name='abc';
$pwd='abc';
if (!empty($_POST['username']) &&  isset($_POST['password')) 
{    
	$myname=$_POST['username'];
	$mypass=$_POST['password'];*/
	
    if ($myname == $name && $mypass==$pwd) 
	{  
		if(!empty($_POST["remember"])) 
		{
			setcookie ("username",$_POST["username"],time()+ 3600);
			setcookie ("password",$_POST["password"],time()+ 3600);
			echo "Cookies Set Successfuly";
		} 
		else if(isset($_COOKIE["username"])) &&  (isset($_COOKIE["username"])) 
		{
			setcookie("username","");
			setcookie("password","");
			echo "Cookies Not Deleted";
		}
		else
		{
			echo "Cookies Not set";  
		}
	}
	else
	{
		header('Location: index.php');
	}
}
/*else
{
    echo "You must supply a username and password.";
}*/
?>