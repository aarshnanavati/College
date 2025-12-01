<!DOCTYPE html>
<html>
<body>

<?php
$date1=date_create("2013-01-01");
$date2=date_create("2019-07-19");
$diff=date_diff($date1,$date2);

// %a outputs the total number of days
echo $diff->format("Total number of days: %a.");
echo "<br>";

// %R outputs + beacause $date2 is after $date1 (a positive interval)
echo $diff->format("Total number of days: %R%a.");
echo "<br>";

// %d outputs the number of days that is not already covered by the month
echo $diff->format("Month: %m, days: %d.<br>");
?>

</body>
</html>


<?php

$interval = new DateInterval('P2Y4DT6H8M'); //where 'P' denotes the period, '2Y' specifies 2 years, '4D' specifies 4 days, '6H' specifies 6 hours, and '8M' specifies 8 minutes.
echo $interval->format('%d days<br>');

?>

<?php

$interval = new DateInterval('P32D');
echo $interval->format('%d days<br>');

?>

<?php

$january = new DateTime('2010-01-01');
$february = new DateTime('2019-02-19');
$interval = $february->diff($january);

// %a will output the total number of days.
echo $interval->format('<br>%a total days')."\n";
echo "<br>";
// While %d will only output the number of days not already covered by the
// month.
echo $interval->format('%m month, %d days');

?>

