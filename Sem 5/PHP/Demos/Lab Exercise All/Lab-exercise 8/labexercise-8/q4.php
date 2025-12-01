<?php
class student
{
    var $name , $rollno , $mark;

    function __construct($n , $r , $m)
    {
        $this->name=$n;
        $this->rollno=$r;
        $this->mark=$m;
    }

    function display()
    {
        echo"<h2> Student detail is given below: <h2>";
        echo "Name is: ". $this->name."<br>";
        echo "Rollno is: ". $this->rollno."<br>";
        echo "Marks is: ". $this->mark."<br>";
    }
}

class result extends student
{
    function grade()
    {
        if($this->mark >= 90)
        {
            echo "A grade";
        }
        elseif($this->mark >= 70)
        {
            echo "B grade";
        }
        elseif($this->mark >= 50)
        {
            echo "C grade";
        }
        else
        {
            echo "U are fail";
        }
    }
    function display1()
    {
        echo $this->grade();
    }   
}

$r = new result("Rushil" , 30 , 70);
$r->display();
$r->display1();

?>