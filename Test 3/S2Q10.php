<?php

class Human {
    public function attack() {
        print "punch";
    }
}

trait Runner {
    public function run() {
        print "Running";
    }
}

class Ninja extends Human {
    use Runner;  
}

class Samurai extends Human {
    use Runner;  
}

$warrior = new Ninja();
$warrior1 = new Samurai();

$warrior->run();  
$warrior1->run(); 

?>
