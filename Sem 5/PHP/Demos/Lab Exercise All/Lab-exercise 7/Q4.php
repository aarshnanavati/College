<?php
// Q4: String Split and Word Count

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = $_POST['input_string'];

    // Split string into characters
    $splitString = str_split($input);
    echo "Split string into characters: <br>";
    foreach ($splitString as $char) {
        echo $char . "<br>";
    }

    // Count words in the sentence
    echo "Word count: " . str_word_count($input) . "<br>";
}
?>

<form method="POST">
    <label for="input_string">Enter a sentence:</label>
    <input type="text" id="input_string" name="input_string">
    <input type="submit" value="Submit">
</form>