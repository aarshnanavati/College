<?php
// List of cities
$cities = ['Paris', 'London', 'New York', 'Tokyo', 'Berlin'];

// Sort cities alphabetically
sort($cities);

// Display sorted cities
echo "Sorted Cities: " . implode(", ", $cities) . "<br>";

// User input for city search
$cityToSearch = readline("Enter a city to search: ");

// Search city
echo (in_array($cityToSearch, $cities) ? "$cityToSearch found" : "$cityToSearch not found") . "<br>";
?>