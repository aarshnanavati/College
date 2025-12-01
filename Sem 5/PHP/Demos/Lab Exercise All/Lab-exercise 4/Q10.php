<?php
function product($x, $y)
{
    return $x * $y;
}

echo "Product = " . product($_POST["num1"], $_POST["num2"]) . "";

?>
