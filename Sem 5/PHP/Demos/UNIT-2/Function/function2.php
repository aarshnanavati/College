

<html>
  <head>
    <title>Function</title>
  </head>
  <body>
    <form action="" method="post">
    Enter 1 number:  
    <input type="number" name="num1" required><br><br>
    Enter 2 number: 
    <input type="number" name="num2" required><br><br>
    <input type="submit" value="submit">
    </form>
  

<?php
  $num1 = $_POST["num1"];
  $num2 = $_POST["num2"];
  function addFunction($num1,$num2)
  {
    $sum = $num1 + $num2;
    echo "Sum of two numbers: ".$sum;
  }
  addFunction($num1,$num2);
?>

</body>
</html>