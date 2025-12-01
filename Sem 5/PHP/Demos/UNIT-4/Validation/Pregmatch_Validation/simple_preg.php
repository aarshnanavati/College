<?php
$my_url = "<b>hello how are you?<b>";
if (preg_match("/you/", $my_url))
{
	echo "the url $my_url contains you"."<br>";
}
else
{
	echo "the url $my_url does not contain you";
}

if (preg_match("/ell/", "Hello World!", $matches)) 
{
  echo "Match was found <br />";
 //echo $matches[0];
}


 if (preg_match("/ll.*/", "The History of Halloween", $matches)) 
 {
  echo "Match was found <br />";
  
  foreach ($matches as $i)
	echo $i."<br>";
  
}
?>
