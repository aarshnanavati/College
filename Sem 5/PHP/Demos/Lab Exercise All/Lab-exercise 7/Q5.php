<?php
// Q5: String Search and Replace

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input = "I love PHP programming";

    // Find position of "PHP"
    $position = strpos($input, "PHP");
    echo "Position of 'PHP': " . $position . "<br>";

    // Replace "PHP" with "Python"
    $replacedString = str_replace("PHP", "Python", $input);
    echo "Replaced string: " . $replacedString . "<br>";
}
?>

<form method="POST">
    <input type="submit" value="Submit">
</form>
