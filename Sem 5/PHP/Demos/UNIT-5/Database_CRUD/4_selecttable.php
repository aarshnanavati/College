<!--
<?php
$servername = "localhost";
$username = "root";
$password = "Root@123";
$db="TYIM";

$conn = new mysqli($servername, $username, $password, $db);	
if(!$conn)
	die("Connection error: " . mysqli_connect_error());
	else
		echo "Connected" . "<br>";
		
	$sql="SELECT userid, addr from customers";
	$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = mysqli_fetch_row($result)) {
        echo "id: " . $row[0]. " " .  "address: " . $row[1]. "<br>";
    }
} else {
    echo "0 results";
}
	//close connection
$conn->close();
?>
-->
	
<?php
$servername = "127.0.0.1:3307";
$username = "root";
$password = "Root@123";
$db="TYIM";

$conn = new mysqli($servername, $username, $password, $db);	
if(!$conn)
	die("Connection error: " . mysqli_connect_error());
	else
		echo "Connected" . "<br>";
		
	$sql="SELECT userid, addr from customers";
	$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
    echo "id: " . $row["userid"]. " address: " . $row["addr"]. "<br>";
}
} else {
    echo "0 results";
}
	//$result->fetch_assoc()
	
	//close connection
$conn->close();
?>
