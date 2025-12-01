<?php
$a = ["red", "green", "blue", "yellow"];
$b = ["green", "yellow", "black"];

$result = array_intersect($a, $b);

print_r($result);
echo "<br>";

$a = ["a" => "red", "b" => "green", "c" => "blue"];
$b = ["a" => "apple", "c" => "cherry"];

$result = array_intersect_key($a, $b);

print_r($result);
echo "<br>";
$a = ["a" => "red", "b" => "green", "c" => "blue"];
$b = ["a" => "red", "b" => "blue", "d" => "green"];

$result = array_intersect_assoc($a, $b);

print_r($result);
