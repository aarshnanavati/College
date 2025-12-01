<?php
$date=date_create("2018-03-15");
echo "1. Now date print in year/month/date\t\t=".date_format($date,"Y/m/d");
echo "<br>";
$date=date_create("15-7-2018");
echo "2. Now date print in year/month/date\t\t=".date_format($date,"Y/m/d");
echo "<br>";
echo "3. Now date print in month/year/date\t\t=".date_format($date,"m/Y/d");
echo "<br>";
date_modify($date,"+15 days");
echo "4. New Modified Date 15 days ahead:\t\t=".date_format($date,"Y-m-d");
echo "<br>";

date_modify($date,"+2 months");
echo "5. New Modified Date 2 months ahead:\t\t=".date_format($date,"Y-m-d");
echo "<br>";

date_modify($date,"-2 days");
echo "6. New Modified Date 2 days before:\t\t=".date_format($date,"Y-m-d");
echo "<br>";

?>
