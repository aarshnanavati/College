<?php
/*
array_change_key_case() function changes the case of all key of an array.
Syntax
array_change_key_case ( array $array [array name,CASE_LOWER/CASE_UPPER ] )  
*/

$Employee_Sal=array("Emp1"=>"50000","Emp2"=>"20000","Emp3"=>"20000");    
print_r(array_change_key_case($Employee_Sal,CASE_LOWER));   

?>    
