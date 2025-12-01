<?php
final class Student {
    public function display() {
        echo "This is a final class. It cannot be inherited.";
    }
}
//the final keyword is used to prevent inheritance of a class or prevent method overriding in child classes.
// Trying to extend Student will cause an error
//class ChildStudent extends Student {} 
$student = new Student();
$student->display();
?>

