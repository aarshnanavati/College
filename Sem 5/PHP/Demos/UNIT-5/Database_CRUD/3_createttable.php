<?php

$servername = "localhost";
$username = "root";
$password = "Root@123";
$db="TYIM";
$conn = new mysqli($servername, $username, $password, $db);	
if(!$conn)
	die("Please check your connection");
	else
		echo "Connected";
	
	$table= "CREATE TABLE product(prodid varchar(10), name varchar(20))";
	//$a = $conn->query($table);
	$a = mysqli_query($conn,$table);
	
	if ($a == TRUE) 
	{
    echo "Table created successfully";
	} 
	else 
	{
    echo "Error creating database: " . mysqli_error($conn);
}

//close connection
$conn->close();

?>
	
