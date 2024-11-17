function Soma-Quadrados-A {
    param ([int]$n)

  $x = 0
  for ($j = 1; $j -le $n ; $j++) {
       $x = $x + ($j * $j)
  }
  return $x
}

function Soma-Quadrados-B {
  param ([int]$n)
  $x = $n * ($n + 1) * (2*$n + 1)
  $x = $x / 6
  return $x
}

$cont=0
while ($cont -lt 10) {
  $valor = Get-Random -Minimum 0 -Maximum 10
  $a = Soma-Quadrados-A -n $valor
  $b = Soma-Quadrados-B -n $valor
  $cor = if ($a -eq $b) {"blue"} else {"red"}
  write-host "Valor=$valor a=$a b=$b" -ForegroundColor $cor
  $cont++
}

