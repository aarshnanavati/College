<?php
// Q9: Difference Between Two Dates
// Define the current date and New Year
$currentDate = new DateTime();
$newYear = new DateTime("first day of January next year"); // Simplified format

// Calculate the difference
$diff = $currentDate->diff($newYear);
echo "Days left until New Year: " . $diff->days . "<br>";
?>