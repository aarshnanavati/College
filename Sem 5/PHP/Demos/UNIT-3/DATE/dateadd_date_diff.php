<?php
echo "the example of date addition and substraction";
echo  "<br><b>".  "Date Add" . "<br></b>";
$date=date_create("2018-03-15");
echo "0. The date is ".date_format($date,"Y-m-d");
echo "<br>";
date_add($date,date_interval_create_from_date_string("4 months + 4 days"));
echo "1. The new added date is ".date_format($date,"Y-m-d");
echo '</br>';
date_add($date,date_interval_create_from_date_string("4 months + 4 days+1 year"));
echo "2. The new added date is ".date_format($date,"Y-m-d");
echo '</br>';
$date1=date_create("2018-03-15");
$date2=date_create("2018-12-18");
$diff=date_diff($date1,$date2);
echo "<br>";

echo "Now differences date is"; echo "<br>";
echo  $diff->y." years" ;echo  "<br>";
echo  $diff->m." months ";echo  "<br>";
echo  $diff->d." days ";

echo "<br>";
$date1=date_create("2018-07-08");
$date2=date_create();
$diff=date_diff($date1,$date2);
echo "<br>";
echo  $diff->y." years ";
echo  $diff->m." months ";
echo  $diff->d." days ";
echo "<br>";
?>

