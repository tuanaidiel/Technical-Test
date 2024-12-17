<?php

echo "Enter milk solids-not-fat (A): ";
$A = trim(fgets(STDIN));

echo "Enter milk fat (B): ";
$B = trim(fgets(STDIN));

$total_milk_solids = $A + $B;

if ($total_milk_solids >= 15 && $B >= 8){
    echo 1;
}
elseif ($total_milk_solids >= 10 && $B >= 3){
    echo 2;
}
elseif ($total_milk_solids >= 3){
    echo 3;
}
else {
    echo 4;
}

?>