function Lista_Primo ([int]$n) {
  #$x = 1
  $A = [System.Collections.ArrayList]@()
  for ($i = 2; $i -le $n; $i++ ) {
    $j = 2
    while (($j -lt $i) -and (($i % $j) -ne 0)) {
        $j = $j + 1
    }
    if ($j -eq $i) {
        $A.Add($j)
      }  
  }
  return $A 
}

$cont=0
while ($cont -lt 1) {
  $valor = Get-Random -Minimum 10 -Maximum 20
  write-host "Valor: $valor Primos: $(Lista_Primo -n $valor)"
  $cont++
}
