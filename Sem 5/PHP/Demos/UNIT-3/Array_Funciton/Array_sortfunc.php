<?php
$values = array(212,32,44,77.90);

$age = array("Ram"=>"50", "Shyam"=>"37", "Vishnu"=>"43");
echo "Shyam is " . $age['Shyam'] . " years old.";

	echo sort($values)."<br>";//ascending to descending
	print_r($values);
	echo "<br>";
	
	echo rsort($values)."<br>";//descending to ascending
	print_r($values);
		echo "<br>";
	
	echo asort($age)."<br>";//ascending to descending
	print_r($age);	
		echo "<br>";
	
	echo arsort($age)."<br>";//descending to ascending
	print_r($age);
		echo "<br>";
	
	echo ksort($age)."<br>"; //A to D Keys
	print_r($age);
		echo "<br>";
	
	echo krsort($age)."<br>";
	print_r($age);
		
	
	
	?>
