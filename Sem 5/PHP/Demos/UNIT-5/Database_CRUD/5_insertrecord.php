<?php
$servername = "localhost";
$username = "root";
$password = "Root@123";
$dbname = "TYIM";

// Create connection
$con = new mysqli($servername, $username, $password, $dbname);

// Check connection
	if(!$con)
		die("Please check your connection");
	else
		echo "Connected";

// SQL query to insert record
$sql = "INSERT INTO customers (userid, addr) VALUES (102, 'Baroda')";
$a = mysqli_query($con,$sql);
if ($a === TRUE) {
    echo "New record inserted successfully";
} else {
    echo "Error creating new records: " . mysqli_error($con);
}

// Close connection
$con->close();
?>
<!--
<?php
$servername = "127.0.0.1:3307";
$username = "root";
$password = "Root@123";
$dbname = "TYIM";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Connected successfully<br>";
}

// SQL query to insert record
$sql = "INSERT INTO customers (userid, addr) VALUES (101, 'Ahmedabad')";

if ($conn->query($sql) === TRUE) {
    echo "New record inserted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close connection
$conn->close();
?>

