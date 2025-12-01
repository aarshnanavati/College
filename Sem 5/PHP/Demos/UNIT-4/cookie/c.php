<?php
// Step 1: Set a cookie
setcookie("username", "Bharti", time() + 6); // Cookie valid for 1 hour

// Step 2: Check if cookie is set
if(isset($_COOKIE["username"])) {
    echo "Welcome back, " . $_COOKIE["username"];
} else {
    echo "Hello, new visitor! Cookie is not set yet.";
}
?>

<!---
 <?php
// Step 1: Create a cookie (valid for 1 hour)
setcookie("username", "Bharti", time() + 3600);

// Step 2: Show cookie if it exists
if(isset($_COOKIE["username"])) {
    echo "Welcome, " . $_COOKIE["username"] . "<br>";
    
    // Step 3: Delete the cookie
    setcookie("username", "", time() - 3600);
    echo "Cookie deleted successfully!";
} else {
    echo "Hello, new visitor! Cookie is not set yet.";
}
?>

