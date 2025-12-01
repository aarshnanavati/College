<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];

    // Regex: only alphabets (upper/lowercase) and numbers, 3 to 15 characters
    if (preg_match("/^[A-Za-z0-9]{3,15}$/", $username)) {
        echo " Valid username: " . ($username);
    } else {
        echo "Invalid username. Use only letters and numbers (3–15 characters).";
    }
}
?>

<html>
<body>
    <h2>Enter Username</h2>
    <form method="post">
        <input type="text" name="username" required>
        <input type="submit" value="Validate">
    </form>
</body>
<!--
Regex Explanation /^[A-Za-z0-9]{3,15}$/

^ → start of string

[A-Za-z0-9] → allows uppercase (A–Z), lowercase (a–z), and numbers (0–9)

{3,15} → length must be between 3 and 15 characters

$ → end of string

Valid examples:

Bharti123

abc123

User99

Invalid examples:

ab (too short, less than 3)

hello_world (underscore not allowed)

bharti@99 (special character not allowed)

abcdefghijklmnop (too long, more than 15)
-->
</html>

