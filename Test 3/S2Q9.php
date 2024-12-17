<?php

class Human {
    public function attack() {
        print "punch";
    }
}

class Ninja extends Human {
  
    public function attack() {
        print "slash";
    }

    public function throw() {
        print "shuriken";
    }
}

$warrior = new Ninja();

$warrior->attack();  
$warrior->throw();   

?>
