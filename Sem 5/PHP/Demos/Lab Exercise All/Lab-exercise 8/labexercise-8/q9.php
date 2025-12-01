<?php
class CartItem
{
    public $name, $price, $quantity;

    public function __construct($name, $price, $quantity)
    {
        $this->name = $name;
        $this->price = $price;
        $this->quantity = $quantity;
    }

    public function getTotalPrice()
    {
        return $this->price * $this->quantity;
    }
}

// Creating cart items
$item1 = new CartItem("Laptop", 50000, 1);
$item2 = new CartItem("Mouse", 500, 2);
$item3 = new CartItem("Keyboard", 1500, 1);

// Store in array
$cart = [$item1, $item2, $item3];
$grandTotal = 0;

foreach ($cart as $item) {
    echo "{$item->name} - Rs.{$item->price} x {$item->quantity} = Rs.{$item->getTotalPrice()}<br>";
    $grandTotal += $item->getTotalPrice();
}

echo "<br> Grand Total: Rs.$grandTotal</br>";
?>