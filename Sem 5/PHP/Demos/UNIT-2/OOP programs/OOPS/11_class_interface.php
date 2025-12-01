<?php
// Define an interface
/*
An interface defines a set of methods that a class must implement.

Unlike abstract classes, an interface cannot have properties or method bodies (only method declarations).

A class can implement multiple interfaces (PHP supports multiple interface inheritance).
*/

interface Person {
    public function setData($name, $age);
    public function display();
}

// Implementing interface in Student class
class Student implements Person {
    private $name;
    private $age;
    private $rollNo;

    public function setData($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    public function setRollNo($rollNo) {
        $this->rollNo = $rollNo;
    }

    public function display() {
        echo "Student Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
        echo "Roll No: " . $this->rollNo . "<br>";
    }
}

// Another class implementing same interface
class Teacher implements Person {
    private $name;
    private $age;
    private $subject;

    public function setData($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    public function setSubject($subject) {
        $this->subject = $subject;
    }

    public function display() {
        echo "Teacher Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
        echo "Subject: " . $this->subject . "<br>";
    }
}

// --- Program Execution ---
$student = new Student();
$student->setData("Riya", 20);
$student->setRollNo(101);
$student->display();

echo "<hr>";

$teacher = new Teacher();
$teacher->setData("Mr. Sharma", 40);
$teacher->setSubject("Computer Science");
$teacher->display();
?>

