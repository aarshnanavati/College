<?php
// PHP program to display the working of str_split()
 
$string = "Geeks";
 
// Since second argument is not passed,
// string is split into substrings of size 1.
print_r(str_split($string));
echo "<br>";
 
$string = "hell how are you?";
 
// Splits string into substrings of size 4
// and returns array of substrings.
print_r(str_split($string, 4));
echo "<br>";

$str=array();
$str= str_split($string,3);
echo $str[0];
echo "<br>";
echo $str[1];
echo "<br>";
echo $str[2];
echo "<br>";
echo $str[3];
echo "<br>";
echo $str[4];
echo "<br>";
echo $str[5];
echo "<br>";
?>
