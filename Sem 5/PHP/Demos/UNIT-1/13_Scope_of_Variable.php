<?php
// Global variable
$x = 10;
static $z = 0;
   
function varscope()
 {
    // Local variable
    $y = 5;
    echo "Local variable y = $y <br>";

  // echo $x; // Undefined variable error

   
    global $x;
    echo "Global variable x = $x <br>";
static $z = 0;
   
   $z++;
    echo "Static variable z = $z <br>";
}

varscope();
varscope();
varscope();
?>
