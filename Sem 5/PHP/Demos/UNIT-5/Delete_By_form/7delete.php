<?php
$servername = "localhost";
$username = "root";
$password = "Root@123";
$db="TYIM";

$conn = new mysqli($servername, $username, $password, $db);	
if(!$conn)
	die("Please check your connection");
	else
		echo "Connected" . "<br>";

	$userid=$_POST['userid'];
	$add=$_POST['add'];

$sql="SELECT userid, addr from customers";
	$result = $conn->query($sql);
	echo "<table border='1'>
	<tr>
		<th>User ID</th>
		<th>Address</th>
	</tr>";


if ($result->num_rows > 0) {
    // output data of each row
  
	while($row = $result->fetch_assoc())
	  {
		  echo "<tr>";
		  echo "<td>" . $row['userid'] . "</td>";
		  echo "<td>" . $row['addr'] . "</td>";
		   echo "</tr>";
	  }
	echo "</table>";
}
$conn->close();

?>

<html>
<body>
<form action="7display.php" method="post">
 <p>User id: <input type="text" name="userid" /></p>
 <p><input type="submit" name="submit" value="submit"/></p>
<p> <input type="reset" value="cancel"> </p>
</form>
</body>
</html>

