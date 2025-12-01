<?php

//Array Slice

$a=array("red","green","blue","yellow","brown");

print_r(array_slice($a,1,2));
echo "<br>";
echo "<br>";
print_r(array_slice($a,-3,1));
echo "<br>";
echo "<br>";

print_r(array_slice($a,1,2,true));
echo "<br>";echo "<br>";echo "<br>";

$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow","e"=>"brown");
print_r(array_slice($a1,1,2));
echo "<br>";
echo "<br>";

$b=array("0"=>"red","1"=>"green","2"=>"blue","3"=>"yellow","4"=>"brown");
print_r(array_slice($b,1,2));


?> 
