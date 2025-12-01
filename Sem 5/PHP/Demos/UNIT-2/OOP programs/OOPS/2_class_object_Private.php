<?php
class Student {
    public $name;
    private $age;
    public function setAge($age) {
        $this->age = $age;
    }

   /* public function getAge() {
        return $this->age;
    }*/

    public function display() {
        echo "Name: " . $this->name . "<br>";
        echo "Age: " . $this->age . "<br>";
    }
}

// Create object
$stu = new Student();
$stu->name = "Anita";    // public attribute can be set directly
$stu->setAge(17);        // private attribute set via method
//$stu->age = 17; 
//$stu->getAge();
// Display details
$stu->display();
?>
