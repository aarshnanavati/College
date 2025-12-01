<?php
// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['setCookies'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Set cookies for 1 hour
        setcookie("username", $username, time() + 3600, "/");
        setcookie("password", $password, time() + 3600, "/");

        echo "Cookies set successfully!<br>";
    }

    if (isset($_POST['deleteCookies'])) {
        // Expire cookies by setting time in the past
        setcookie("username", "", time() - 3600, "/");
        setcookie("password", "", time() - 3600, "/");

        echo "Cookies deleted successfully!<br>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Set & Delete Cookies Example</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="post" action="">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" name="setCookies" value="Set Cookies">
        <input type="submit" name="deleteCookies" value="Delete Cookies">
    </form>

    <br>
    <?php
    // Display cookies if available
    if (isset($_COOKIE["username"]) && isset($_COOKIE["password"])) {
        echo "Stored Cookies:<br>";
        echo "Username: " . $_COOKIE["username"] . "<br>";
        echo "Password: " . $_COOKIE["password"] . "<br>";
    } else {
        echo "No cookies found.";
    }
    ?>
</body>
</html>

