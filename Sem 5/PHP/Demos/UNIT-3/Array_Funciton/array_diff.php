<?php
$a = ["red", "green", "blue", "yellow"];
$b = ["green", "yellow"];

$result = array_diff($a, $b);

print_r($result);
echo "<br>";

$num1 = [10, 20, 30, 40];
$num2 = [20, 40, 50];

$result = array_diff($num1, $num2);


print_r($result);
echo "<br>";

$a = ["a" => "red", "b" => "green", "c" => "blue"];
$b = ["a" => "pink", "c" => "yellow"];

$result = array_diff_key($a, $b);

print_r($result);
?>
