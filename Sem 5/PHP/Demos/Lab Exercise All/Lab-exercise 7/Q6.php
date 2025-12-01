<?php
// Q6: Tokenizing a String

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = $_POST['input_string'];

    // Tokenize the string
    $token = strtok($input, ",");
    while ($token !== false) {
        echo $token . "<br>";
        $token = strtok(",");
    }
}
?>

<form method="POST">
    <label for="input_string">Enter comma-separated values:</label>
    <input type="text" id="input_string" name="input_string" required>
    <input type="submit" value="Submit">
</form>