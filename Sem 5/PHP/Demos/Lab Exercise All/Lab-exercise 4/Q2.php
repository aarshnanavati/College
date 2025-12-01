<?php

$num = $_POST["num"];

switch ($num) {
    case 1:
        echo "Monday";
        break;
    case 2:
        echo "Tuesday";
        break;
    case 3:
        echo "Wedneday";
        break;
    case 4:
        echo "Thursday";
        break;
    case 5:
        echo "Friday";
        break;
    case 6:
        echo "Saturdyay";
        break;
    case 7:
        echo "Sunday";
        break;
    default:
        echo "Not a valid number";

}
?>