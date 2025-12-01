<?php
$email = "test@example.com";
if (preg_match("/^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}$/", $email)) 
{
    echo "Valid Email";
} 
else 
{
    echo "Invalid Email";
}
?>
