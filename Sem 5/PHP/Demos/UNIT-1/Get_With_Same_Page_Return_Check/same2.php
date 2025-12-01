<?php
	if(isset($_GET["sub"]))
	{
 		echo $_GET["uname"];
	}
  
 
?>
<html>
<head>
    <title>User Input Form</title>
</head>
<body>
  <!--  <h2>Enter Your Name</h2>-->
    <form action=" " method="get">
       
        <label for="username">
        Enter User Name:
        </label>
        
        <input type="text" name="uname" >
       
        <input type="submit" value="Submit" name="sub">
    </form>
</body>
</html>

