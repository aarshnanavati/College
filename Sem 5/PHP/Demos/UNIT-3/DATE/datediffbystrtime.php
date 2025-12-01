<?php
$daysLeft = 0;
$fromDate = "2018-07-15";
$curDate = date('Y-m-d');

$daysLeft = strtotime($curDate) - strtotime($fromDate);
echo $daysLeft."<br>";
$days = $daysLeft/(60 * 60 * 24);

echo "Days difference", $days;
?>
