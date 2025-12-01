<?php
/*
array_rand($arr)

This function randomly selects one element from the given array and returns it.

In case of indexed array, it will return the index of the element, 
in case of associative array, it will return the key of the selected random element.
*/



$colors = array("red", "black", "blue", "green", "white", "yellow");

echo "Color of the day: ". $colors[array_rand($colors)];

?>
    