<?php
interface  paymentgateway
{
    public function processpayment($amt);
}

class paypal implements paymentgateway
{
    function processpayment($amt)
    {
        echo "Processing amt is:".$amt."<br>";
    }
}

class creditpayment implements paymentgateway
{
    function processpayment($amt)
    {
        echo "Credit amt is:".$amt."<br>";
    }
}

$obj = new paypal();
$obj1 = new creditpayment();

$obj->processpayment(3000);
$obj1->processpayment(1000);
?>