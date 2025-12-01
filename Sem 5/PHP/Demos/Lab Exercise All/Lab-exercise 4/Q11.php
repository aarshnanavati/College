<?php
function reverseWord($w)
{
    return strrev($w);
}
echo "Reverse: " . reverseWord($_POST['a']);
?>