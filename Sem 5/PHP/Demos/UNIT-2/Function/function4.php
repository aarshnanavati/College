


<?php
function setHeight($minheight, $temp = 50)
{
    echo "The height is : $minheight . $temp <br>";
}

setHeight(350,10);
setHeight(); // will use the default value of 50
setHeight(135);
setHeight(80);
?>