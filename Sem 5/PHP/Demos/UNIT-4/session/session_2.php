<?php
  
   session_start();
?>
<html>
<body>
      
      <h2>Enter Username and Password</h2> 
	<?php
         /*  $msg = '';
            
            if (isset($_POST['login']) && !empty($_POST['username']) && !empty($_POST['password'])) 
	    {
				
               if ($_POST['username'] == 'abc' && $_POST['password'] == '1234')
		 {
               
                  $_SESSION['username'] = 'abc';
                  
                  echo 'You have entered valid use name and password';
		  echo "<br>";
		  echo "Welcome  ".   $_SESSION['username'];
               }
		else
		 {
                  $msg = 'Wrong username or password';
               }
            }*/
         ?>
<form action = "session3.php" method = "post">
          
            <input type = "text" class = "form-control" 
               name = "username" required autofocus></br>
            <input type = "password" class = "form-control"
               name = "password"  required>
            <button class = "btn btn-lg btn-primary btn-block" type = "submit" 
               name = "login">Login</button>
         </form>
			
         
         
     
      
   </body>
</html>
