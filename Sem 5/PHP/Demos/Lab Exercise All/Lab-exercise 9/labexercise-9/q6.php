<?php
$str = "apple,orange;banana|grape";
$parts = preg_split("/[,;|]/", $str);
print_r($parts);

?>