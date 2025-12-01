<?php
// Declare and initialize array with values from 1 to 10
$numbers = range(1, 10);

// Calculate sum and average
$sum = array_sum($numbers);
$average = $sum / count($numbers);

// Output results
echo "Sum: $sum<br>";
echo "Average: $average<br>";
?>