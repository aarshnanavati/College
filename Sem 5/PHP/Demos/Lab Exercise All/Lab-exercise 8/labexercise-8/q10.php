<?php
// Abstract class
abstract class Shape {
    abstract public function area();
}

// Interface
interface Printable {
    public function printDetails();
}

// Circle
class Circle extends Shape implements Printable {
    private $radius;
    public function __construct($r) {
        $this->radius = $r;
    }
    public function area() {
        return 3.14 * $this->radius * $this->radius;
    }
    public function printDetails() {
        echo "Circle with radius {$this->radius}, Area = " . $this->area() . "<br>";
    }
}

// Square
class Square extends Shape implements Printable {
    private $side;
    public function __construct($s) {
        $this->side = $s;
    }
    public function area() {
        return $this->side * $this->side;
    }
    public function printDetails() {
        echo "Square with side {$this->side}, Area = " . $this->area() . "<br>";
    }
}

// Triangle
class Triangle extends Shape implements Printable {
    private $base, $height;
    public function __construct($b, $h) {
        $this->base = $b;
        $this->height = $h;
    }
    public function area() {
        return 0.5 * $this->base * $this->height;
    }
    public function printDetails() {
        echo "Triangle with base {$this->base}, height {$this->height}, Area = " . $this->area() . "<br>";
    }
}

// Demonstration
$shapes = [
    new Circle(5),
    new Square(4),
    new Triangle(6, 8)
];

foreach ($shapes as $shape) {
    $shape->printDetails();
}
?>
