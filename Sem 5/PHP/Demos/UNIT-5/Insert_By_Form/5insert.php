<?php
$servername = "localhost";
$username = "root";
$password = "Root@123";
$db="TYIM";

$con = new mysqli($servername, $username, $password, $db);	
if(!$con)
	die("Please check your connection");
	else
		echo "Connected" . "<br>";

$userid=$_POST['userid'];
$add=$_POST['add'];
	
$sql="INSERT INTO customers(userid,addr) VALUES('$userid','$add')";
// $a = mysqli_query($con,$sql);
// if ($a === TRUE) {
//     echo "New record inserted successfully";
// } else {
//     echo "Error creating new records: " . mysqli_error($con);
// }

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$con->close();
?>



    