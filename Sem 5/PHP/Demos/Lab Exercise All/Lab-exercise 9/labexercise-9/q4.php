<?php
$str = "Order number is 12345 and price is 500";
preg_match_all("/\d+/", $str, $matches);
print_r($matches[0]);
?>