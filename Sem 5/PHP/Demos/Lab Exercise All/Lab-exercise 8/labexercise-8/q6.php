<?php
abstract class libraryitem
{
    abstract function getdetails();
    abstract function borrowitem();
}
class uploadlibraray extends libraryitem
{
    function getdetails()
    {
        $this->book = "Rushil";
        return $this->book;

        $this->money = 400;
        return $this->money;
    }
    function borrowitem()
    {
        echo "This book hs been borowed";
    }
}
$obj = new uploadlibraray();
$obj->getdetails();
$obj->borrowitem();
?>