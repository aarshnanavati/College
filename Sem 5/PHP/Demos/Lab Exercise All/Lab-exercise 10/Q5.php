<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['remember'])) {
        setcookie("username", $_POST['username'], time() + (86400 * 30), "/"); // 30 days
    }
    echo "Logged in as " . $_POST['username'];
}
?>

<form method="POST" action="">
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    Remember Me: <input type="checkbox" name="remember"><br>
    <input type="submit" value="Login">
</form>

<?php
// Autofill username if the cookie is set
if (isset($_COOKIE['username'])) {
    echo "Hello, " . $_COOKIE['username'] . " (from cookie).";
}
?>