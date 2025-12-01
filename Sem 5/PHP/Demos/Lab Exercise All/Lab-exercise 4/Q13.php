<?php
$n = $_POST['n'];
if ($n % 2 == 0 && $n % 3 == 0)
    echo "$n divisible by both 2 and 3";
elseif ($n % 2 == 0)
    echo "$n divisible by 2";
elseif ($n % 3 == 0)
    echo "$n divisible by 3";
else
    echo "$n not divisible by 2 or 3";
?>