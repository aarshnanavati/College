<?php
 
// PHP program to illustrate substr()
function Substring($str){
    $len = strlen($str);
    echo $str;
    echo "<br>";
    echo $len;
    echo "<br>";
    echo substr($str, 8);
    echo "<br>";
    echo substr($str, 6, $len);
    echo "<br>";
    echo substr($str, -5, 10);
    echo "<br>";
    echo substr($str,-8, -5);
    echo "<br>";
}
 
// Driver Code
$str="hello how are you?";
Substring($str);
 
?>