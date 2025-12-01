<?php
    $con = mysqli_connect("localhost", "root", "Root@123", "TYIM");
    if (!$con)
        die("Please check your connection");
    else
        echo "Connected";
echo "enter user id and address for update";
    $userid = $_POST['userid'];
    $add = $_POST['add'];

    // Correct mysqli_query for update
    $sql1 = "UPDATE customers SET addr='$add' WHERE userid='$userid'";
    $result = mysqli_query($con, $sql1);

    // Fetch all records
    $sql = "SELECT * FROM customers";
    $result = mysqli_query($con, $sql);

    echo "<table border='1'>
    <tr>
        <th>User ID</th>
        <th>Address</th>
    </tr>";

    while ($row = mysqli_fetch_array($result)) {
        echo "<tr>";
        echo "<td>" . $row['userid'] . "</td>";
        echo "<td>" . $row['addr'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";

    mysqli_close($con);
?>

