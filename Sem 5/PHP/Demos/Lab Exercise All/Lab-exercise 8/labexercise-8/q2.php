<?php
class bankacc{
    public $accNumber , $balance;

    function __construct($a,$b)
    {
        $this->accNumber=$a;
        $this->balance=$b;
    }

    function deposit($amt)
    {
        if ($amt > 0)
        {
            $this->balance += $amt;
            echo "Deposited ₹$amt into Account <br>";
        }
        else
        {
            echo "Deposit amount must be greater than 0 <br>";
        }

    }

    function withdraw($amt)
    {
        if ($amt > 0 && $amt <= $this->balance)
        {
            $this->balance -= $amt;
            echo "Withdraw ₹$amt from Account<br>";
        } 
        else 
        {
            echo "Insufficient balance <br>";
        }
    }

    function getbalance()
    {
        return $this->balance;
    }
}
$obj = new bankacc(123,20000);
$obj1 = new bankacc(1234,1000);

$obj->withdraw(2000);
$obj->deposit(10000);
echo "Final Balance in Account 1: ₹" . $obj->getBalance() . "<br><br>";

$obj1->withdraw(1000);
$obj1->deposit(500);
echo "Final Balance in Account 2: ₹" . $obj1->getBalance() . "<br>";
?>