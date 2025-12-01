<?php
// Set cookie for 1 day
setcookie("user", "admin", time() + 86400, "/"); // Expires in 1 day

// Check if the cookie is set
if (isset($_COOKIE['user'])) {
    echo "Stored username in cookie: " . $_COOKIE['user'];
} else {
    echo "Cookie is not set!";
}

// Delete cookie by setting expiry time in the past
if (isset($_GET['delete'])) {
    setcookie("user", "", time() - 3600, "/"); // Expired cookie
    echo "Cookie has been deleted.";
}
?>

<a href="?delete=true">Delete Cookie</a>