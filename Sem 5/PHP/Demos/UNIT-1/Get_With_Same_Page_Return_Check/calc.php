<?php
if (isset($_GET["sub"])) 
{
    if (empty($_GET["num1"]) && empty($_GET["num2"])) 
    {
        echo "Enter Number";
    }
    else
    {
        $num1 = intval($_GET["num1"]);
        $num2 = intval($_GET["num2"]);
        echo $num1 - $num2;
    }
} 
if (isset($_GET["add"])) 
{
    if (empty($_GET["num1"]) && empty($_GET["num2"])) 
    {
        echo "Enter Number";
    }
    else
    {
        $num1 = intval($_GET["num1"]);
        $num2 = intval($_GET["num2"]);
        echo $num1 + $num2;
    }
} 
?>
<html>
<head>
    <title>User Input Form</title>
</head>
<body>
    <h2>Enter Your Name</h2>
    <form action=" " method="get">
       
        <label for="username">
        Enter User Name:
        </label>
        
        <input type="text" name="num1" >
	<input type="text" name="num2" >

       
        <input type="submit" value="+" name="add">
	<input type="submit" value="-" name="sub">

    </form>
</body>
</html>

