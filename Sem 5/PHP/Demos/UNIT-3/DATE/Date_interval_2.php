
<?php
$interval=new DateInterval('P5Y4M2DT5H3M4S');
echo "%Y Years : ".$interval->format('%Y Years')."<br>";
echo "%y Years : ".$interval->format('%y Years')."<br>";
echo "%M Months : ".$interval->format('%M Months')."<br>";
echo "%m Months : ".$interval->format('%m Months')."<br>";
echo "%D Days : ".$interval->format('%D Days')."<br>";
echo "%d Days : ".$interval->format('%d Days')."<br>";

echo "%H Hours : ".$interval->format('%H Hours')."<br>";
echo "%h Hours : ".$interval->format('%h Hours')."<br>";

echo "%I Minutes : ".$interval->format('%I Minutes')."<br>";
echo "%i MInutes : ".$interval->format('%i Minutes')."<br>";

echo "%S Seconds : ".$interval->format('%S Seconds')."<br>";
echo "%s Seconds : ".$interval->format('%s Seconds')."<br>";

//echo "%F Microseconds : ".$interval->format('%F Microseconds')."<br>";  // PHP 7
//echo "%f Microseconds : ".$interval->format('%f Microseconds')."<br>"; // PHP 7

?>
