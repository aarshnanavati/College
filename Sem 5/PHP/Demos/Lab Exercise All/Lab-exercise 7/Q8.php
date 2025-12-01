<?php
// Q8: Creating Dates

// Using mktime() to create a custom date
$customDate = mktime(10, 30, 0, 8, 15, 2025);
echo "Custom date: " . date("l, d-M-Y h:i A", $customDate) . "<br>";

// Using strtotime() to create a custom date
$customDateStr = strtotime("15 August 2025 10:30 am");
echo "Custom date from strtotime: " . date("l, d-M-Y h:i A", $customDateStr) . "<br>";
?>