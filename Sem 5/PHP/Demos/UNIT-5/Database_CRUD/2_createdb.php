<?php
    $con = mysqli_connect("localhost","root","");
    if(!$con)
    {
        die("Please check your connection");
    }
    else
    {
        echo "Connection Successful";
    }

    $sql = "CREATE DATABASE IF NOT EXISTS TYIM";
   if(mysqli_query($con,$sql))
   {
    echo "<br>Database Created";
   }
   else
   {
    echo "<br>Error in creating database".mysqli_error($con);
   }
   
    $con -> close();
?>