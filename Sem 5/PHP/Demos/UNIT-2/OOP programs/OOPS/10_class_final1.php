<?php
class Person {
    public function showInfo() {
        echo "This is a normal method.<br>";
    }

    final public function display() {
        echo "This is a final method. Child classes cannot override it.<br>";
    }
}

class Student extends Person {
    // This works fine
    public function showInfo() {
        echo "Student information here.<br>";
    }

    // If we try to override display(), PHP will throw an error
    /*
    public function display() {
        echo "Trying to override final method.";
    }
    */
}

$student = new Student();
$student->showInfo();   // allowed
$student->display();    // final method from parent
$student1 = new Person();
$student1->showInfo(); 
$student1->display();    // final method from parent

?>

