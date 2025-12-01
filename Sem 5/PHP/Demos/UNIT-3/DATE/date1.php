<?php
echo "1. Current year now in four digits\t\t=".date("Y");
echo "<br>";
echo "2. Current year last two digits\t\t=".date("y");
echo "<br>";
echo "3. Current year month in digits \t\t=".date("m");echo "<br>";
echo "4. Current year month in three  char \t\t=".date("M");echo "<br>";
echo "5. Current year day in three  char. \t\t=".date("D");echo "<br>";
echo "6. Current date in two digits\t\t\t=".date("d");echo "<br>";
echo "14.Current date in second two digits\t\t\t=".date("j");echo "<br>";
echo "7. Current Full date\t\t\t=".date("r");echo "<br>";
echo "8. Current time meridiam in small letters\t\t\t=".date("a");echo "<br>";
echo "9. Current time meridiam in capital letters\t\t\t=".date("A");echo "<br>";
echo "10.Current time in hour two digits\t\t\t=".date("g"); echo "<br>";
echo "11.Current time in hour two digits\t\t\t=".date("G");echo "<br>";
echo "12.Current time in minute two digits\t\t\t=".date("i"); echo "<br>";
echo "13.Current time in second two digits\t\t\t=".date("s");echo "<br>"; 
echo "15. Current year day in all  char. \t\t=".date("l");echo "<br>";
echo "16. Current year month in all  char. \t\t=".date("F");echo "<br>";
echo "17. A numeric representation of the day (0 for Sunday, 6 for Saturday)\t\t\t".date("w");echo "<br>";
echo "18. The day of the year (from 0 through 365)\t\t\t".date("z");echo "<br>";
echo "19. A numeric representation of a month, without leading zeros (1 to 12)\t\t\t".date("n");echo "<br>";
echo "20. The number of days in the given month\t\t\t".date("t");echo "<br>";
echo "<br>";echo "<br>";echo "<br>";echo "<br>";
echo "Today is " . date("d/m/y") . "<br>";
echo "Today is " . date("Y.m.d") . "<br>";
echo "Today is " . date("Y-m-d") . "<br>";
echo "Today is " . date("l");echo "<br>";
echo "<br>";
echo "The date-time is " . date("h:i:sa");
echo "<br>";

echo time();echo "<br>";
//“$timezone_identifiers = DateTimeZone::listIdentifiers();” calls the listIdentifiers static method of the DateandTime Zone built in class. 
echo "The time in " . date_default_timezone_get() . " is " . date("H:i:s");
echo "<br>";
date_default_timezone_set("Africa/Accra");
echo "The time in " . date_default_timezone_get() . " is " . date("H:i:s");
?> 

