<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $password = $_POST['password'];

    // Regex: strong password rules
    if (preg_match("/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/", $password)) {
        echo "Strong password set successfully!";
    } else {
        echo " Weak password. Must contain:<br>
              - Minimum 8 characters<br>
              - At least one uppercase letter<br>
              - At least one lowercase letter<br>
              - At least one number<br>
              - At least one special character (@$!%*?&)";
    }
}
?>

<html>
<body>
    <h2>Create a Password</h2>
    <form method="post">
        <input type="password" name="password" required>
        <input type="submit" value="Validate">
    </form>
</body>
<!--
Regex Explanation

/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/

^ → start of string

(?=.*[a-z]) → must contain at least one lowercase

(?=.*[A-Z]) → must contain at least one uppercase

(?=.*\d) → must contain at least one digit

(?=.*[@$!%*?&]) → must contain at least one special character

[A-Za-z\d@$!%*?&]{8,} → allowed characters, with minimum length 8

$ → end of string

 Valid examples:

Bharti@123

HelloWorld1!

Test@2025

 Invalid examples:

password (no uppercase, number, or special char)

Pass123 (too short, no special char)

HELLO@123 (no lowercase)
-->
</html>

