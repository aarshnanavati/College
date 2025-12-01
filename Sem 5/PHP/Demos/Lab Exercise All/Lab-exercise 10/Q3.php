<?php
session_start();

// Set session variables
if (!isset($_SESSION['name'])) {
    $_SESSION['name'] = 'John Doe';
    $_SESSION['email'] = 'john.doe@example.com';
    echo "Session variables are set.<br>";
}

// Modify email
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $_SESSION['email'] = $_POST['new_email'];
    echo "Email updated!<br>";
}

// Unset email variable
if (isset($_GET['unset'])) {
    unset($_SESSION['email']);
    echo "Email session variable has been unset.<br>";
}
?>

<form method="POST" action="">
    New Email: <input type="email" name="new_email" required><br>
    <input type="submit" value="Update Email">
</form>

<a href="?unset=true">Unset Email</a>