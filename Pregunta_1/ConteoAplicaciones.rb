# Valor global para contar las aplicaciones
$i = 0

# Método para contar las aplicaciones
def dist(n)
  $i += 1
  if n == 2 || n == 1
    return 1
  elsif n % 2 == 0
    dist(n / 2)
  else
    dist(3 * n + 1)
  end
end

# Método llamar al método dist y mostrar el valor de la variable global
def count(n)
  dist(n)
  puts($i)
end

# Agregar el número que se desea contar
count(42)