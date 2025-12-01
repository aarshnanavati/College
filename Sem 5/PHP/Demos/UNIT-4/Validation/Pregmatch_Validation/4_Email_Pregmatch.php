<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];

    // Regex for validating email
    if (preg_match("/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/", $email)) {
        echo "Valid email: " . ($email);
    } else {
        echo "Invalid email format. Please enter a correct email.";
    }
}
?>

<html>
<body>
    <h2>Enter Your Email</h2>
    <form method="post">
        <input type="text" name="email" required>
        <input type="submit" value="Validate">
    </form>
</body>
<!--
Regex Explanation

/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/

^ → start of string

[A-Za-z0-9._%+-]+ → allows letters, numbers, dot ., underscore _, percent %, plus +, and hyphen - before @

@ → must contain @ symbol

[A-Za-z0-9.-]+ → domain name (e.g., gmail, yahoo, outlook)

\. → literal dot before domain extension

[A-Za-z]{2,} → domain extension (like com, in, org – at least 2 letters)

$ → end of string

 Valid examples:
user@example.com

bharti123@gmail.com

test.user99@yahoo.co.in

 Invalid examples:

user@.com (missing domain name)

@gmail.com (missing username)

hello@gmail (missing .com or extension)
-->
</html>

