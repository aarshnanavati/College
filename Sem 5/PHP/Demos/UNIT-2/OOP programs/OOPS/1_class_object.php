<?php
class Student {
    public $name;
    public $age;

    public function display() {
        echo "Name: $this->name, Age: $this->age";
    }
}

// Create object
$stu = new Student();
$stu->name = "Rahul";
$stu->age = 16;

// Call method
$stu->display();
?>
