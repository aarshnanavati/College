<?php

/*
array_merge($arr1, $arr2)
using this function we can combine them into one single array. */
$Array1 = array("Maruti","Honda", "Hyundai", "Toyoto" );

// friends who own the above cars
$Array2 = array("800", "City", "Grandi20", "Tiago");

// let's merge the two arrays into one
$merged = array_merge($Array1, $Array2);

print_r($merged);

?>
