function Primo {
    param ([int]$n)

  $j = 2
  while (($j -lt $n) -and (($n % $j) -ne 0) ) {
    $j++
  }
  if ($j -eq $n) {
    write-host "$n e primo" -ForegroundColor Red
  }
  else {
    write-host "$n nao e primo" -ForegroundColor Blue
  }
}

Install-Module -Name Graphical
Import-Module -Name Graphical
$cont=4
#pega
[int[]]$datapoints =@(0)*31
while ($cont -le 30) {
  $datapoints[$cont] = ((1..5 | Measure-Command -Expression {Primo -n $cont}).TotalMilliseconds | Measure-Object -Average).Average * 100
  $cont++
}

Show-Graph -Type Bar -GraphTitle "Desempenho Algoritmo Detecta Primos" -XAxisTitle "Valor de N" -YAxisTitle "Tempo Médio (deciseg)" -Datapoints $datapoints