<?php

// array_column(array $array, string|int|null $column_key, string|int|null $index_key = null): array

$records = [
    ["id" => 1, "name" => "GLS", "age" => 25],
    ["id" => 2, "name" => "BCOM", "age" => 30],
    ["id" => 3, "name" => "BBA", "age" => 35]
];

$names = array_column($records, "name");

print_r($names);
echo "<br>";
$records = [
    ["id" => 1, "name" => "Alice", "age" => 25],
    ["id" => 2, "name" => "Bob", "age" => 30],
    ["id" => 3, "name" => "Charlie", "age" => 35]
];

$names = array_column($records, "name", "id");

print_r($names);
?>
