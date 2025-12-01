<?php
// Base class
class Person {
    public $name;
    public $age;

    public function setPerson($name, $age) {
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

    public function setStudent($name, $age, $rollNo, $className) {
        // Call parent method
        $this->setPerson($name, $age);
        $this->rollNo = $rollNo;
        $this->className = $className;
    }

    public function displayStudent() {
        $this->displayPerson(); // from parent class
        echo "Roll No: " . $this->rollNo . "<br>";
        echo "Class: " . $this->className . "<br>";
    }
}

// --- Program Execution ---
$student1 = new Student();
$student1->setStudent("Riya", 20, 101, "iMSc IT");

$student2 = new Student();
$student2->setStudent("Aman", 21, 102, "iMSc IT");

$student1->displayStudent();
echo "<hr>";
$student2->displayStudent();
?>

