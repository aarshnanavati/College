<?php
  
   session_start();
?>
<html>
<body>
      
      <h2>Enter Username and Password</h2> 
	
<form action = "session3.php" method = "post">
          
            <input type = "text" name = "username" required autofocus></br>
            <input type = "password" name = "password"  required>
            <button type = "submit" name = "login">Login</button>
         </form>
			
         
        
     
      
   </body>
</html>
