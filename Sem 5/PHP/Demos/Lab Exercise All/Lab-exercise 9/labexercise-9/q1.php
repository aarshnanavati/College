<?php
$text = "I love PHP programming!";
if (preg_match("/php/i", $text)) 
{
    echo "Yes, 'php' found!";
}
?>