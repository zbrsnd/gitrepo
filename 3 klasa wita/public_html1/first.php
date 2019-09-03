<!DOCTYPE html>
<html lang="pl">

<head>
<meta charset="utf-8" />
<title>bez nazwy</title>
<meta name="generator" content="Geany 1.32" />
</head>

<body>
    
<?php
echo "Witaj!";
//zmienne globalne
$x = 5 * 5;
$txt = "działania"; 

function myTest() {
    global $x, $txt
    if ($x > 20) # .$TXT.  <--- PRZYKŁAD ŁĄCZENIA ELEMENTÓW PRZEZ PHP
        echo "<p>Wynik ".$txt.": $x </p>"; # PODWÓJNE CUDZYSŁOWY W PHP MÓWIĄ, ŻE CIĄG TEKSTOWY MOŻE ZAWIERAĆ ZMIENNE DO ZINTERPRETOWANIA
    
    
    
}


?> 

</body>

</html>
