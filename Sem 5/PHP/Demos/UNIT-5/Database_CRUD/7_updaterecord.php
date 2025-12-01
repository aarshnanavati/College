<?php
$servername = "localhost";
$username = "root";
$password = "Root@123";
$dbname = "TYIM";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to update record
$sql = "UPDATE customers SET addr = 'Mumbai' WHERE userid = 101";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

// Close connection
$conn->close();
?>

