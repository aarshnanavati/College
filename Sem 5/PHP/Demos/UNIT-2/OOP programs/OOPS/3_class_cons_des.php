<?php
class Student {
    public $name;

    public function __construct($name) {
        $this->name = $name;
        echo "Constructor: Student $this->name is created.<br>";
    }

    public function __destruct() {
        echo "Destructor: Student $this->name is destroyed.<br>";
    }
    public function display() {
        echo "Hello, my name is $this->name.<br>";
    }
}
$stu1 = new Student("Rahul");
$stu1->display();

$stu2 = new Student("Anita");
$stu2->display();
?>
