<?php

/*array_shift($arr)

This function can be used to remove/shift the first element out of the array. 
*/
$Car_Name = array("Maruti", "Honda", "Morris Garrage");
print_r($Car_Name);
echo "<br>";
// removing the first element
array_shift($Car_Name);

print_r($Car_Name);
echo "<br>";

/*
Similar to this, we have another function array_unshift($arr, $val) 
to add a new value($val) at the start of the array(as the first element).
*/
$Car_Name = array("Maruti", "Honda", "Morris Garrage");
print_r($Car_Name);
echo "<br>";
array_unshift($Car_Name,"Tiago","Suzuki","Swift");

print_r($Car_Name);
?>
