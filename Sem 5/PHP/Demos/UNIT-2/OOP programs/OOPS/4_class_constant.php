<?php
class Student {
    const SCHOOL = "GLS School";
    public $name;
   /* public function __construct($name) {
        $this->name = $name;
    }*/
     public function get($name)
    {
     $this->name = $name;
     }

    public function display() {
        echo "Name: " . $this->name . "<br>";
        echo "School: " . self::SCHOOL . "<br>"; // Accessing constant inside class
    }
}

echo "School Name (from class): " . Student::SCHOOL . "<br><br>";
// Create object
//$stu = new Student("Rahul");

$stu = new Student();
$stu->get("Rahul");
$stu->display();

?>
