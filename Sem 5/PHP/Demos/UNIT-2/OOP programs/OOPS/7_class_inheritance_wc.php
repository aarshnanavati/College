<?php
// Base class
class Person {
    public $name;
    public $age;

    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    public function displayPerson() {
        echo "Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
    }
}

// Derived class (Inheritance)
class Student extends Person {
    public $rollNo;
    public $className;

    public function __construct($name, $age, $rollNo, $className) {
        // Call parent constructor
        parent::__construct($name, $age);
        $this->rollNo = $rollNo;
        $this->className = $className;
    }

    public function displayStudent() {
        $this->displayPerson(); // From parent class
        echo "Roll No: " . $this->rollNo . "<br>";
        echo "Class: " . $this->className . "<br>";
    }
}
/*
// Another class to group students
class Classroom {
    public $className;
    public $students = [];

    public function __construct($className) {
        $this->className = $className;
    }

    public function addStudent(Student $student) {
        $this->students[] = $student;
    }

    public function showClassroom() {
        echo "<h3>Classroom: " . $this->className . "</h3>";
        foreach ($this->students as $student) {
            $student->displayStudent();
            echo "<hr>";
        }
    }
}*/

// --- Program Execution ---
$student1 = new Student("Riya", 20, 101, "MSc IT");
$student2 = new Student("Aman", 21, 102, "MSc IT");
$student1->displayStudent();
$student2->displayStudent();
/*
$classroom = new Classroom("MSc IT - Year 1");
$classroom->addStudent($student1);
$classroom->addStudent($student2);

$classroom->showClassroom();
*/
?>

