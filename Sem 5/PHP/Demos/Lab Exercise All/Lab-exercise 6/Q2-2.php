<?php
// Initialize array
$numbers = [];

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect the input values from the form
    for ($i = 0; $i < 8; $i++) {
        $numbers[] = (int) $_POST['number' . $i];
    }

    // Find largest and smallest numbers
    $largest = max($numbers);
    $smallest = min($numbers);

    // Output results
    echo "Largest number: $largest<br>";
    echo "Smallest number: $smallest<br>";
} else {
    // Display form to accept user input
    echo '<form method="POST">';
    echo 'Enter 8 numbers:<br>';
    for ($i = 0; $i < 8; $i++) {
        echo 'Number ' . ($i + 1) . ': <input type="number" name="number' . $i . '" required><br>';
    }
    echo '<input type="submit" value="Submit">';
    echo '</form>';
}
?>