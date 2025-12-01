<?php
$m = $_POST["m"];
$s = $_POST["s"];
$e = $_POST["e"];

$total = $m + $e + $s;
$perc = $total / 3;

echo "Total marks are : $total <br><br>";
echo "Percentage is : $perc <br><br>";

if ($perc >= 80) {
    echo "Grade A";
} else if ($perc >= 60) {
    echo "Grade B";
} else if ($perc >= 50) {
    echo "Grade C";
} else {
    echo "Scored very less focus moree !!!!!";
}
?>