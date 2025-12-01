<?php
$name = "Riya";
$math = 85;
$science = 90;
$english = 78;

$total = $math + $science + $english;
$percentage = $total / 3;

$report = <<<REPORT
<h2>Student Report</h2>
<p><strong>Name:</strong> $name</p>
<p><strong>Math:</strong> $math</p>
<p><strong>Science:</strong> $science</p>
<p><strong>English:</strong> $english</p>
<p><strong>Total:</strong> $total</p>
<p><strong>Percentage:</strong> $percentage%</p>
<hr>
REPORT;

echo $report;
?>
