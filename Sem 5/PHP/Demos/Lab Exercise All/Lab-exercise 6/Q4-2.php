<?php
// Define two 2D arrays (matrices)
$matrix1 = [
    [1, 2],
    [3, 4]
];
$matrix2 = [
    [5, 6],
    [7, 8]
];

// Perform matrix addition
$sumMatrix = [];
for ($i = 0; $i < 2; $i++) {
    for ($j = 0; $j < 2; $j++) {
        $sumMatrix[$i][$j] = $matrix1[$i][$j] + $matrix2[$i][$j];
    }
}

// Display result
echo "Matrix 1:<br>";
foreach ($matrix1 as $row) {
    echo implode(" ", $row) . "<br>";
}
echo "Matrix 2:<br>";
foreach ($matrix2 as $row) {
    echo implode(" ", $row) . "<br>";
}
echo "Sum Matrix:<br>";
foreach ($sumMatrix as $row) {
    echo implode(" ", $row) . "<br>";
}
?>
