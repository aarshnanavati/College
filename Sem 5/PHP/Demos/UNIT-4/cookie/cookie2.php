 <?php
// set the expiration date to one hour ago
if(isset($_COOKIE['user']))
{
setcookie("user", "", time() - 0.2 );
}
else
{
	echo "cookie not available";
}
?>
<html>
<body>

<?php
echo "Cookie 'user' is deleted.";
?>

</body>
</html> 
