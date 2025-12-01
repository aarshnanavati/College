 <?php
$cookie_n = "user";
$cookie_value = "abcd";
setcookie($cookie_n, $cookie_value, time() + 180); // 86400 = 1 day
?>
<html>
<body>

<?php
if(!isset($_COOKIE[$cookie_n])) {
    echo "Cookie named '" . $cookie_n . "' is not set!";
} else {
    echo "Cookie '" . $cookie_n. "' is set!<br>";
    echo "Name is: " . $_COOKIE[$cookie_n];
      
}
?>

</body>
</html> 