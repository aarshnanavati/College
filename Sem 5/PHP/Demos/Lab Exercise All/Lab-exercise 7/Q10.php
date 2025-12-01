<?php
// Q10: Get Date Information

// Get current date information
$dateInfo = getdate();

// Display date information
echo "Current year: " . $dateInfo["year"] . "<br>";
echo "Current month: " . $dateInfo["month"] . "<br>";
echo "Current weekday: " . $dateInfo["weekday"] . "<br>";
echo "Current day of the month: " . $dateInfo["mday"] . "<br>";
?>