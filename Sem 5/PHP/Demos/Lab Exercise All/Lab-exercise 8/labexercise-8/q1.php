<?php
class emp
{
    var $name, $id, $salary;

    function set_data($name)
    {
        $this->name = $name;
    }

    function set_data1($id)
    {
        $this->id = $id;
    }

    function set_data2($salary)
    {
        $this->salary = $salary;
    }

    function get_data()
    {
        return $this->name;
    }

    function get_data1()
    {
        return $this->id;
    }

    function get_data2()
    {
        return $this->salary;
    }
}

$people = new emp();
$people->set_data("Rushil");
$people->set_data1(1);
$people->set_data2(20000);

echo "Name is: " . $people->get_data() . "<br>";
echo "Id is: " . $people->get_data1() . "<br>";
echo "Salary is: " . $people->get_data2() . "<br>";
?>