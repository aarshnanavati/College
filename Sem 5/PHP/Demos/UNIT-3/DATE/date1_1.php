<?php
//today date and time
// Mountain Standard Time (MST) Time Zone

$today = date("F j, Y, g:i a");  
echo $today."<br>";               // July 11, 2019, 4:58 pm
$today = date("m.d.y");
echo $today."<br>";                          // 07.11.19
$today = date("j, n, Y"); 
echo $today."<br>";                       // 11, 7, 2019
$today = date("Ymd");
echo $today."<br>";                            // 20190711
$today = date('h-i-s, j-m-y, it is w Day');
echo $today."<br>";      // 04-58-41, 11-07-19, 5831 5841 4 Thupm19
$today = date('\i\t \i\s \t\h\e jS \d\a\y.');
echo $today."<br>";    // it is the 11th day.
$today = date("D M j G:i:s T Y"); 
echo $today."<br>";               // Thu Jul 11 16:58:41 IST 2019
$today = date('H:m:s \m \i\s\ \m\o\n\t\h'); 
echo $today."<br>";     // 16:07:41 m is month
$today = date("H:i:s");  
echo $today."<br>";                        // 16:58:41
$today = date("Y-m-d H:i:s");  
 echo $today."<br>";                 // 2019-07-11 17:00:38 (the MySQL DATETIME format)
?>
