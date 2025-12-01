<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number'];

    // Regex: only digits (0-9), 5 to 10 digits long
    if (preg_match("/^[0-9]{5,10}$/", $number)) {
        echo "Valid number: " . ($number);
    } else {
        echo "Invalid number. Please enter only digits (5–10 characters).";
    }
}
?>

<html>
<body>
    <h2>Enter Number</h2>
    <form method="post">
        <input type="text" name="number" required>
        <input type="submit" value="Validate">
    </form>
</body>
<!--
Regex Explanation /^[0-9]{5,10}$/

^ → start of string

[0-9] → only numbers allowed (digits 0–9)

{5,10} → must be between 5 and 10 digits long

$ → end of string

Valid examples:

12345

9876543210

Invalid examples:

123 (too short)

123456789012 (too long)

123a45 (contains a letter)
-->
</html>

