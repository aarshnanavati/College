
<?php 
$tim=time();
echo($tim . "<br>");
echo(date("H-s-i",$tim));

// Create DateTime object 
$date = new DateTime('2018-09-15'); 
 echo "<br>"; 
// Set the new DateTime 
$date->setTime(12, 30); 
   echo "<br>"; 

// Display the date in given format 
echo $date->format('d-m-Y H:i:s') . "\n"; 
   echo "<br>"; 
// Set the new DateTime 
$date->setTime(12, 30, 20); 
   echo "<br>"; 
// Display the date in given format 
echo $date->format('Y-m-d H:i:s'); 
?> 

