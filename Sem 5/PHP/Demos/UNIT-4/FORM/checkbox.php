<?php

	 

	 if(isset($_POST['hobbies']))
	 {
		 echo "<h2> You have selected: </h2>";

	 	 foreach($_POST['hobbies'] as $hobby)
		 {

			echo "<p>".$hobby ."</p>"; //Print all the hobbies

	 
		 }
	}

	 else
	{

		 echo "<b>Please Select at least One Hobby.</b>";

	 }

	 

	?>
