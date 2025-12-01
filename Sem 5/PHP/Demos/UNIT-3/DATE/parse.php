<?php
//parse a date(changing a format)
$dateTime = strtotime('Apr 30, 2010');
echo date('Y-m-d', $dateTime);
echo "<br>";echo "<br>";echo "<br>";echo "<br>";
print_r(date_parse("2006-12-12 10:00:00.5"));
echo "<br>";echo "<br>";
//$det=date();
$new_det=getdate(date("U"));
print_r ($new_det);
?>
