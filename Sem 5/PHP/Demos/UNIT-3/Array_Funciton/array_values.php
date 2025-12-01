<?php
/*
array_values($arr)

If we want to take all the values from our array, without the keys, 
and store them in a separate array, then we can use array_values() function.
*/



$hatchbacks = array(
        "Suzuki" => "Baleno",
        "Skoda" => "Fabia",
        "Hyundai" => "i20",
        "Tata" => "Tigor"
    );

// friends who own the above cars
$friends = array("Vinod", "Javed", "Navjot", "Samuel");

// let's merge the two arrays into one
$merged = array_merge($hatchbacks, $friends);

//getting only the values
$merged = array_values($merged);

print_r($merged);

?>
