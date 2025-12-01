<?php
function EO($n)
{
    if ($n % 2 == 0) {
        echo "Number is even";
    } else {
        echo "Number is Odd";
    }

}
echo $_POST['n'] . " is " . EO($_POST['n']);
?>