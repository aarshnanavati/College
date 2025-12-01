<?php
// Setting a cookie
$cookie_name = "user";
$cookie_value = "Bharti Shah";
// setcookie(name, value, expire, path, domain, secure, httponly);
setcookie($cookie_name, $cookie_value, time() + (86400 * 7), "/"); // expires in 7 days

// Accessing the cookie

if(isset($_COOKIE[$cookie_name])) {
    echo "Cookie '" . $cookie_name . "' is set!<br>";
    echo "Value is: " . $_COOKIE[$cookie_name];
} else {
    echo "Cookie named '" . $cookie_name . "' is not set!";
}

?>

