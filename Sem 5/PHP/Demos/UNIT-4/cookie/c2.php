<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Set cookies for 1 day
    setcookie("username", $username, time() + 3600, "/");
    setcookie("password", $password, time() + 3600, "/");

    echo "Cookies set successfully!<br>";
    echo "Username: " . $username . "<br>";
    echo "Password: " . $password . "<br>";
}
?>

<html>
<head>
    <title>Set Cookies Example</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="post" action="">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" value="Set Cookies">
    </form>

    <br>
    <?php
    // Display cookies if already set
    if (isset($_COOKIE["username"]) && isset($_COOKIE["password"])) {
        echo "Stored Cookies:<br>";
        echo "Username: " . $_COOKIE["username"] . "<br>";
        echo "Password: " . $_COOKIE["password"] . "<br>";
    }
    ?>
</body>
</html>

