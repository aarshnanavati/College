<?php
function fact($n)
{
    $f = 1;
    for ($i = 1; $i <= $n; $i++)
        $f *= $i;
    return $f;

}
echo "Factorial = " . fact($_POST['n']);
?>