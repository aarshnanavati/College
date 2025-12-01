<?php
            $msg = '';
            
            if (isset($_POST['login']) && !empty($_POST['username']) && !empty($_POST['password'])) 
	    {
				
               if ($_POST['username'] == 'abc' && $_POST['password'] == '1234')
		 {
               
                  $_SESSION['username'] = $_POST['username'] ;
                  
                  echo 'You have entered valid use name and password';
		  echo "<br>";
		  echo "Welcome   ".   $_SESSION['username'];
               }
		else
		 {
                  $msg = 'Wrong username or password';
		  echo $msg;
               }
            }
	    
?>
Click here to clean <a href = "logout.php" tite = "Logout">Session.