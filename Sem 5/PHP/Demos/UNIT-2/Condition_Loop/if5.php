<html>
   <body>
   
      <?php
      
         $d = date("D");
	echo $d;
	echo "<br>";
	
         if ($d == "Tue")
            echo "Have a nice weekend!"; 
	elseif($d == "Sat")
		echo "Tomorrow sunday!!";
	else
            echo "Have a nice day!"; 
      ?>
   
   </body>
</html>