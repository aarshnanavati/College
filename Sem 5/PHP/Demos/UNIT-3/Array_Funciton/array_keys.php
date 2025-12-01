<?php


/*array_keys($arr)
Just like values, we can also extract just the keys from an array. 
*/

$Sur_Name = array(
        "Bharti" => "Shah",
        "Poonam" => "Dang",
        "Jyoti" => "Dubey",
        "Monica" => "Gupta"
    );

$New_Name = array("Nirav", "Anjali", "Jainin", "Garima");

$merged = array_merge($Sur_Name, $New_Name);

//getting only the values
$values = array_values($merged);
//getting only the keys
$keys = array_keys($merged);
print_r($values);
echo "<br>";
echo "<br>";
print_r($keys);



?> 
