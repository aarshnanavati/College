<!-- <html>
   
   <head>
      <title>Passing Argument by Reference</title>
   </head>
   
   <body>
<?php

//Defining a function that multiply a number by itself and return the new value

function selfMultiply(&$number){
    $number *= $number;
    return $number;
}
 
$mynum = 5;
echo "Only the define number$mynum<br>"; // Outputs: 5
 
selfMultiply($mynum);
echo "Global number$mynum<br>"; // Outputs: 25


 function addten($num) {
            $num += 10;
	    echo "Inside function: $num<br>";
         }
         
         function addSix(&$num) {
            $num += 6;
         }
         
         $orignum = 10;
         addten( $orignum );
         
         	echo "Original Value is $orignum<br />";
         
         addSix( $orignum );
       	  echo "Original Value is $orignum<br />";
      ?>
      
   </body>
</html> -->
<?php
function addFive(&$number) {
    $number += 5;
}

$value = 10;
addFive($value);

echo "Value after function call: $value";  // Output: Value after function call: 15
?>
