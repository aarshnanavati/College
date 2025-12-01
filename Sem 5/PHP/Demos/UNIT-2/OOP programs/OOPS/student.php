<?php

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


class Student extends Person {
    public $rollNo;

    public function setStudent($name, $age, $rollNo) {
        $this->setPerson($name, $age);  
        $this->rollNo = $rollNo;
    }

    public function displayStudent() {
        $this->displayPerson();
        echo "Roll Number: " . $this->rollNo . "<br>";
    }
}


$stu = new Student();
$stu->setStudent("Mira", 5, 101);
$stu->displayStudent();
?>