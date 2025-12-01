<?php
// First interface
interface Person {
    public function setData($name, $age);
    public function display();
}

// Second interface
interface Sports {
    public function setSport($sportName);
}

// Third interface
interface Marks {
    public function setMarks($marks);
}

// Class implementing multiple interfaces
class Student implements Person, Sports, Marks {
    private $name;
    private $age;
    private $sport;
    private $marks;

    // From Person interface
    public function setData($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    // From Sports interface
    public function setSport($sportName) {
        $this->sport = $sportName;
    }

    // From Marks interface
    public function setMarks($marks) {
        $this->marks = $marks;
    }

    // From Person interface
    public function display() {
        echo "Student Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
        echo "Sport: " . $this->sport . "<br>";
        echo "Marks: " . $this->marks . "<br>";
    }
}

// --- Program Execution ---
$student = new Student();
$student->setData("Riya", 20);
$student->setSport("Badminton");
$student->setMarks(89);

$student->display();
?>

