<?php
$num = $_POST['num'];
if ($num > 0) {
    echo "$num is possitive";
} elseif ($num < 0) {
    echo "$num is negative";
} else {
    echo "Number is zero !";
}

?>