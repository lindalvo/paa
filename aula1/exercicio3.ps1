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

$cont=0
while ($cont -lt 1000) {
  $valor = Get-Random -Minimum 0 -Maximum 1000
  Primo -n $valor
  $cont++
}
