<?php
// Q2: Trimming Strings

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = $_POST['input_string'];

    // Display trimmed strings
    echo "Leading spaces removed: '" . ltrim($input) . "'<br>";
    echo "Trailing spaces removed: '" . rtrim($input) . "'<br>";
    echo "Both ends trimmed: '" . trim($input) . "'<br>";
}
?>

<form method="POST">
    <label for="input_string">Enter a string with spaces:</label>
    <input type="text" id="input_string" name="input_string">
    <input type="submit" value="Submit">
</form>