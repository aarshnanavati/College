<?php
$string = "Hello world. Beautiful day today.";
$token = strtok($string, " ");
 echo "$token<br />";
$token1 = strtok(" ");
 echo "$token1<br />";
 $token2= strtok(" ");
 echo "$token2<br />";
 $token3 = strtok(" ");
 echo "$token3<br />";
 $token4= strtok(" ");
 echo "$token4<br />";

 
 
 
 /*  $string = 'Hey there buddy';
    $t = strtok($string,' ');
    while($t != false)
    {
        echo $t."<br/>";
        $t= strtok(' ');
    }
*/
?>