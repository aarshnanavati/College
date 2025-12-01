 <?php
echo "1. The time is " . date("h:i:s:A");
echo "<br>";
$d=mktime(11,14, 54, 8, 12, 2014); //mktime(hour,minute,second,month,day,year);
echo "2. Created date is " . date("Y-m-d h:i:sa", $d);
echo "<br>";
$d=mktime(-16, 14, 54, 8, 12, 2014); //mktime(hour,minute,second,month,day,year);
echo "3. Created date is " . date("Y-m-d h:i:sa", $d);
echo "<br>";
$d=mktime();
echo "4. Created date is " . date("Y-m-d h:i:sa", $d);
echo "<br>";

$endTime = mktime(23, 59, 59, 12, 31, date('Y')-1);   
echo "5. Created date is " . date("Y-m-d h:i:sa", $endTime);
echo "<br>";
$futureDate = mktime(0, 0, 0, date("m")+3, date("d"), date("Y"));
echo "6. Created date is " .date("d/m/Y", $futureDate);echo "<br>";
?>
