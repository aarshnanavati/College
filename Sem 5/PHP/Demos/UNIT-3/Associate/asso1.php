<?php

// One way to create an associative array 
$name_one = array("Ram"=>"Sita", "Krishna"=>"Radha",  
                  "Raja"=>"Rani", "Akabar"=>"Birbal",  
                  "Rammohan"=>"Tenaliram"); 
  
// Second way to create an associative array 
$name_two["Ram"] = "Sita"; 
$name_two["Krishna"] = "Radha"; 
$name_two["Raja"] = "Rani"; 
$name_two["Akabar"] = "Birbal"; 
$name_two["Rammohan"] = "Tenaliram"; 
  
// Accessing the elements directly 
echo "Accessing the elements directly:\n"; 
echo $name_two["Ram"], "\n"; 
echo $name_two["Krishna"], "\n"; 
echo $name_two["Raja"], "\n"; 
echo $name_one["Akabar"], "\n"; 
echo $name_one["Rammohan"], "\n"; 
  
?> 
