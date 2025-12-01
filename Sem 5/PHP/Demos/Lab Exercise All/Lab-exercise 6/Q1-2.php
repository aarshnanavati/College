<?php
// Initialize array
$numbers = [];

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect the input values from the form
    for ($i = 0; $i < 5; $i++) {
        $numbers[] = (int) $_POST['number' . $i];
    }

    // Print array in reverse order
    echo "Numbers in reverse order:<br>";
    for ($i = count($numbers) - 1; $i >= 0; $i--) {
        echo $numbers[$i] . "<br>";
    }
} else {
    // Display form to accept user input
    echo '<form method="POST">';
    echo 'Enter 5 numbers:<br>';
    for ($i = 0; $i < 5; $i++) {
        echo 'Number ' . ($i + 1) . ': <input type="number" name="number' . $i . '" required><br>';
    }
    echo '<input type="submit" value="Submit">';
    echo '</form>';
}
?>