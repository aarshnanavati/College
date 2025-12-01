    <?php  
    function adder(&$str2)  
    {  
        $str2 .= 'Call By Reference';
        
    }  
    $str = 'Hello ';  
    adder($str);  
    echo $str."<br>";  
    ?>  


    <?php  
    function sayHello($name="Sonoo"){  
    echo "Hello $name<br/>";  
    }  
    sayHello("Rajesh");  
    sayHello();//passing no value  
    sayHello("John");  
    ?>  


<?php  
function cube($n){  
return $n*$n*$n;  
}  
echo "Cube of 3 is: ".cube(3);  
?> 
