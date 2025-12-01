 <html>
<body>

<?php
if(count($_COOKIE) > 0) {
    echo "Cookies are enabled.";
    echo count($_COOKIE);
} else {
    echo "Cookies are disabled.";
}
?>

</body>
</html> 