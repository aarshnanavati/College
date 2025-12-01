<?php
// Base class
class Vehicle {
    public $brand;
    public $model;

    function __construct($brand, $model) {
        $this->brand = $brand;
        $this->model = $model;
    }

    // Method to be overridden
    function displayInfo() {
        echo "This is a vehicle.<br>";
    }
}

// Subclass Car
class Car extends Vehicle 
{
    function displayInfo() 
    {
        echo "Car - Brand: $this->brand, Model: $this->model <br>";
    }
}

// Subclass Bike
class Bike extends Vehicle {
    function displayInfo() {
        echo "Bike - Brand: $this->brand, Model: $this->model <br>";
    }
}

// Subclass Truck
class Truck extends Vehicle {
    function displayInfo() {
        echo "Truck - Brand: $this->brand, Model: $this->model <br>";
    }
}

// Store objects in an array
$vehicles = [
    new Car("Toyota", "Camry"),
    new Bike("Yamaha", "R15"),
    new Truck("Tata", "407")
];

// Display all details using loop
echo "<h2>Vehicle Showroom Details</h2>";
foreach ($vehicles as $v) 
{
    $v->displayInfo();   // Polymorphism in action
}
?>
