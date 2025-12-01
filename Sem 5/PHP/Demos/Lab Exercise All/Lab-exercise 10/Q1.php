<?php
session_start();

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Simple validation
    if ($username == 'admin' && $password == 'password123') {
        $_SESSION['username'] = $username;
        echo "Welcome, " . $_SESSION['username'] . "!";
    } else {
        echo "Invalid credentials!";
    }
}

// Logout
if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: " . $_SERVER['PHP_SELF']);
}
?>

<form method="POST" action="">
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <input type="submit" value="Login">
</form>

<?php if (isset($_SESSION['username'])): ?>
    <a href="?logout=true">Logout</a>
<?php endif; ?>