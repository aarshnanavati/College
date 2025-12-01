<html>
<body>

<?php
echo(strtotime("now") . "<br>");echo "<br>";
echo(strtotime("3 October 2005") . "<br>");
echo(strtotime("+5 hours") . "<br>");
echo(strtotime("+1 week") . "<br>");
echo(strtotime("+1 week 3 days 7 hours 5 seconds") . "<br>");
echo(strtotime("next Monday") . "<br>");
echo(strtotime("last Sunday"));
echo "<br>";
$d=strtotime("3 October 2005");
echo "String to time Created date is " . date("Y-m-d h:i:sa", $d);
echo "<br>";
$d=strtotime("now");
echo "String to time Created date is " . date("Y-m-d h:i:sa", $d);
$d1=strtotime("+1 week");
echo "<br>";
echo "String to time Created date is " . date("Y-m-d h:i:sa", $d1);
echo "<br>";
$d2=strtotime("+1 week 3 days 7 hours 5 seconds");
echo "String to time Created date is " . date("Y-m-d h:i:sa", $d2); 
echo "<br>";
$d3=strtotime("- 1 week 7 hours 5 seconds"); 
echo "String to time Created date is " . date("Y-m-d h:i:sa", $d3); 
?>

</body>
</html>
