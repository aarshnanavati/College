<?php
class Department {
    final public function displayDept() {
        echo "This is a Department.<br>";
    }
}

class CSEDepartment extends Department 
{
    public function show() {
        echo "This is CSE Department (cannot override displayDept).<br>";
    }
}

// Demonstration
$dept = new Department();
$dept->displayDept();

$cse = new CSEDepartment();
$cse->displayDept();  // From parent
$cse->show();         // Own method
?>
