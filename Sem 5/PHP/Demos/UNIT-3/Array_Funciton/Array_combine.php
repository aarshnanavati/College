<?php
$keys = ["name", "age", "city"];
$values = ["GLS", 98, "Ahmedabad"];

$result = array_combine($keys, $values);
//Warning: array_combine(): Both parameters should have an equal number of elements
print_r($result);

$fruits = ["apple", "banana", "cherry"];
echo "<br>"."total elements in the array are". count($fruits);  

$fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];
$result = array_count_values($fruits);
echo "<br>";
print_r($result);
?>

