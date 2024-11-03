# Metodo para unir dos arreglos en cuanto a un orden ascendente
def merge(left, right)
  result = []
  # Mientras ambos arreglos tengan elementos
  until left.empty? || right.empty?
    # Se compara el primer elemento de cada arreglo
    # Si el primer elemento del arreglo izquierdo es menor o igual al primer elemento del arreglo derecho, se agrega el primer elemento del arreglo izquierdo al arreglo resultante y se elimina del arreglo izquierdo
    # Si el primer elemento del arreglo derecho es menor al primer elemento del arreglo izquierdo, se agrega el primer elemento del arreglo derecho al arreglo resultante y se elimina del arreglo derecho
    result << (left.first <= right.first ? left.shift : right.shift)
  end
  # Se agrega el arreglo izquierdo y derecho al arreglo resultante
  result + left + right
end

# Método para dividir un arreglo en dos partes y llamar al método merge
def mergesort(array)
  # Si el arreglo tiene un elemento o no tiene elementos, se retorna el arreglo
  if array.length <= 1
    return array
  else
    # Se obtiene el índice medio del arreglo
    # Se divide el arreglo en dos partes: izquierda y derecha
    mid = (array.length / 2).floor
    left = mergesort(array[0...mid])
    right = mergesort(array[mid...array.length])
    # Se llama al método merge para unir los arreglos izquierdo y derecho
    merge(left, right)
  end
end

# Método principal
def main()
  # Se llama al método mergesort con un arreglo desordenado y se muestra el arreglo ordenado
  result = mergesort([42, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10])
  puts(result.inspect)
end

main()

# El algoritmo divide en dos partes el arreglo y llama al método merge para unir los arreglos izquierdo y derecho en cuanto a un orden ascendente
# Una decisio de implementacion fue utilizar el método shift para eliminar el primer elemento de un arreglo
# Otra decisión de implementación fue tomar los elementos de la mitad menos uno del arreglo para el arreglo izquierdo y los elementos de la mitad hasta el final del arreglo para el arreglo derecho