<?php
// Abstract class
abstract class Person {
    public $name;
    public $age;

    // Abstract method (no body here)
    abstract public function display();

    // Normal method
    public function setPerson($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }
}

// Child class (must implement abstract method)
class Student extends Person {
    public $rollNo;

    public function setStudent($name, $age, $rollNo) {
        $this->setPerson($name, $age);
        $this->rollNo = $rollNo;
    }

    // Implement abstract method
    public function display() {
        echo "Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
        echo "Roll No: " . $this->rollNo . "<br>";
    }
}

// Another child class
class Teacher extends Person {
    public $subject;

    public function setTeacher($name, $age, $subject) {
        $this->setPerson($name, $age);
        $this->subject = $subject;
    }

    // Implement abstract method
    public function display() {
        echo "Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
        echo "Subject: " . $this->subject . "<br>";
    }
}

// --- Program Execution ---
$student = new Student();
$student->setStudent("Riya", 20, 101);
$student->display();

echo "<hr>";

$teacher = new Teacher();
$teacher->setTeacher("Mr. Sharma", 40, "Computer Science");
$teacher->display();
?>

