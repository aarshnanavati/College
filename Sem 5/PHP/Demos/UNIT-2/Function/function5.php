



<?php
function sum($x, $y) 
{
    $z = $x + $y;
    return $z;
}

$t = sum(10,25);
echo $t;
echo "5 + 10 = " . sum(5, 10) . "<br>";
echo "7 + 13 = " . sum(7, 13) . "<br>";
echo "2 + 4 = " . sum(2, 4);
?>