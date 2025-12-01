<?php
// Q1: String Length and Reverse

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = $_POST['input_string'];

    // Display string length
    echo "Length of the string: " . strlen($input) . "<br>";

    // Display reversed string
    echo "Reversed string: " . strrev($input) . "<br>";
}
?>

<form method="POST">
    <label for="input_string">Enter a string:</label>
    <input type="text" id="input_string" name="input_string">
    <input type="submit" value="Submit">
</form>