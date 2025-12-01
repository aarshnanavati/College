<?php
// Q3: Case Conversion

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = $_POST['input_string'];

    echo "Uppercase: " . strtoupper($input) . "<br>";
    echo "Lowercase: " . strtolower($input) . "<br>";
    echo "Capitalized words: " . ucwords($input) . "<br>";
    echo "Capitalized first character: " . ucfirst($input) . "<br>";
}
?>

<form method="POST">
    <label for="input_string">Enter a string:</label>
    <input type="text" id="input_string" name="input_string">
    <input type="submit" value="Submit">
</form>