<?php
// Start the session
session_start();

// Set session variable if not set
if (!isset($_SESSION['username'])) {
    $_SESSION['username'] = "Bharti";  // you can take input from form also
}

// Display the session variable
echo "Welcome, " . $_SESSION['username'] . "!<br>";

// Provide a logout link to destroy session
echo "<a href='New_Logout.php'>Logout</a>";
?>

