function Lista_Primo ([int]$n) {
  #$x = 1
  $A = [System.Collections.ArrayList]@()
  for ($i = 2; $i -le $n; $i++ ) {
    $j = 2
    while (($j -lt $i) -and (($i % $j) -ne 0)) {
        $j = $j + 1
    }
    if ($j -eq $i) {
        $void = $A.Add($j)
      }  
  }
  return $A 
}

[int[]]$datapoints =@(0)*101
$cont=2
while ($cont -le 100) {
  $datapoints[$cont] = ((1..5 | Measure-Command -Expression {Lista_Primo -n $cont}).TotalMilliseconds | Measure-Object -Average).Average * 100
  $cont++
}

Show-Graph -Type Bar -GraphTitle "Desempenho Algoritmo Lista Primos" -XAxisTitle "Valor de N" -YAxisTitle "Tempo Médio (deciseg)" -Datapoints $datapoints