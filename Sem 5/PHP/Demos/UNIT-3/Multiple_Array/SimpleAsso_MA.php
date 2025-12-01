<html>
<body>

	<?php
	 $marks = array( "raj" => array ("physics" => 35,"maths" => 30, "chemistry" => 39),
	                 "ram" => array ("physics" => 30,"maths" => 32, "chemistry" => 29),
                        "rahul" => array ("physics" => 31, "maths" => 22, "chemistry" => 30));

		   /* Accessing multi-dimensional array values */
		
		   echo "Marks for ram in physics : " ;
		   echo $marks['ram']['physics'] . "<br />"; 
		   echo "Marks for raj in maths : ";
		   echo $marks['raj']['maths'] . "<br />"; 
		   echo "Marks for rahul in chemistry : " ;
		   echo $marks['rahul']['chemistry'] . "<br />"; 
		   print_r($marks);
	?>
</body>
</html>
