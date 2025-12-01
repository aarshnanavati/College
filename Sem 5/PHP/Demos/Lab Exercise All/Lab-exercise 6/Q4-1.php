<?php
// Create 2D array (3x3 matrix)
$matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Print matrix
echo "Matrix:<br>";
foreach ($matrix as $row) {
    echo implode(" ", $row) . "<br>";
}
?>