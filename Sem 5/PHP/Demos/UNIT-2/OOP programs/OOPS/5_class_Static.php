<?php
class Student {
    public static function welcomeMessage() {
        echo "Welcome to GLS School!<br>";
    }

    public $name;

  /*  public function __construct($name) {
        $this->name = $name;
    }*/
    public function get($name)
    {
     $this->name = $name;
     }

    public function display() {
        echo "Student Name: " . $this->name . "<br>";
    }
}

Student::welcomeMessage();

//$stu = new Student("Rahul");
$stu = new Student();
$stu->get("Rahul");
$stu->display();
Student::welcomeMessage();
?>
