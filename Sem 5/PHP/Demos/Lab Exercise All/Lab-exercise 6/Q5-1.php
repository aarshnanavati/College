<?php
// Initialize an array
$cities = ['Paris', 'London', 'New York', 'Tokyo'];

// Count
echo "Count: " . count($cities) . "<br>";

// Merge
$cities2 = ['Berlin', 'Sydney'];
$mergedCities = array_merge($cities, $cities2);
echo "Merged Cities: " . implode(", ", $mergedCities) . "<br>";

// Push and Pop
array_push($cities, 'Rome');
echo "Cities after push: " . implode(", ", $cities) . "<br>";
array_pop($cities);
echo "Cities after pop: " . implode(", ", $cities) . "<br>";

// Search
echo "Search 'London': " . (array_search('London', $cities) !== false ? 'Found' : 'Not Found') . "<br>";

// Sort
sort($cities);
echo "Sorted Cities: " . implode(", ", $cities) . "<br>";

// Check if element exists
echo "Is 'Paris' in array? " . (in_array('Paris', $cities) ? 'Yes' : 'No') . "<br>";
?>