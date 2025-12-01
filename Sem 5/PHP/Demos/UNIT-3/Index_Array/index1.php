<html>
   <body>
   
      <?php
         		/* First method to create array. */
         $first = array( 10, 20, 30, 40, 50);
                  foreach( $first as $v ) 
         {
            echo "Value is $v <br />";
         }
         
        			 /* Second method to create array. */
         $first[0] = "one";
         $first[1] = "two";
         $first[2] = "three";
         $first[3] = "four";
         $first[4] = "five";
         
         foreach( $first as $value )
         {
            echo "Value is $value <br />";
         }
         
         $total = count($first); 
         for($n = 0; $n < $total; $n++)
         { 
   		 echo $first[$n], "\n"; 
	} 
      ?>
      
   </body>
</html>
