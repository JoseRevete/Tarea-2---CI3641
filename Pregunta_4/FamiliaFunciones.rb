require 'benchmark'
require 'csv'

# X: 0, Y: 4, Z: 0
# alpha: 7, beta: 7


# Función recursiva
def recursion(n)
  if 0 <= n && n < 49
    return n
  else
    result = recursion(n - 7) + recursion(n - 14) + recursion(n - 21) + recursion(n - 28) + recursion(n - 35) + recursion(n - 42) + recursion(n - 49)
    return result
  end
end




# Función iterativa
def iterativo(n)
  if 0 <= n && n < 49
    return n
  else
    dicResult = {}
    dicResult[n] = 0
    for i in 0..48
      dicResult[i] = i
    end
    for i in 49..n
      dicResult[i] = dicResult[i - 7] + dicResult[i - 14] + dicResult[i - 21] + dicResult[i - 28] + dicResult[i - 35] + dicResult[i - 42] + dicResult[i - 49]
    end
    return dicResult[n]
  end
end




# Función recursiva de cola
def recursion_cola(n)
  dicResult = {}
  for i in 0..48
    dicResult[i] = i
  end

  def recursion_cola_aux(n, dicResult, key)
    if key > n
      return dicResult[n]
    else
      dicResult[key] = dicResult[key - 7] + dicResult[key - 14] + dicResult[key - 21] + dicResult[key - 28] + dicResult[key - 35] + dicResult[key - 42] + dicResult[key - 49]
      return recursion_cola_aux(n, dicResult, key + 1)
    end
  end

  return recursion_cola_aux(n, dicResult, 49)
end



def main()
  values = [25, 50, 75, 100, 125]
  results = []

  values.each do |n|
    puts ""
    puts "----------------------------------- n = #{n} -----------------------------------"
    puts ""
    iterativo_result = nil
    iterativo_time = Benchmark.realtime { iterativo_result = iterativo(n) }
    puts "Iterativo: #{iterativo_result}, Tiempo: #{iterativo_time} segundos"

    recursivo_result = nil
    recursivo_time = Benchmark.realtime { recursivo_result = recursion(n) }
    puts "Recursivo: #{recursivo_result}, Tiempo: #{recursivo_time} segundos"

    recursivo_cola_result = nil
    recursivo_cola_time = Benchmark.realtime { recursivo_cola_result = recursion_cola(n) }
    puts "Recursivo de Cola: #{recursivo_cola_result}, Tiempo: #{recursivo_cola_time} segundos"

    results << [n, iterativo_time, recursivo_time, recursivo_cola_time]
  end

  CSV.open("resultados.csv", "w") do |csv|
    csv << ["n", "iterativo_time", "recursivo_time", "recursivo_cola_time"]
    results.each { |row| csv << row }
  end

  generate_html(results)
end

def generate_html(results)
  File.open("resultados.html", "w") do |file|
    file.puts <<-HTML
<!DOCTYPE html>
<html>
<head>
  <title>Comparación de tiempos de ejecución</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <h1>Comparación de tiempos de ejecución</h1>
  <canvas id="myChart" width="400" height="200"></canvas>
  <script>
    const labels = #{results.map { |row| row[0] }};
    const data = {
      labels: labels,
      datasets: [
        {
          label: 'Iterativo',
          data: #{results.map { |row| row[1] }},
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          fill: false
        },
        {
          label: 'Recursivo',
          data: #{results.map { |row| row[2] }},
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
          fill: false
        },
        {
          label: 'Recursivo de Cola',
          data: #{results.map { |row| row[3] }},
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          fill: false
        }
      ]
    };

    const config = {
      type: 'line',
      data: data,
      options: {
        scales: {
          x: {
            beginAtZero: true
          },
          y: {
            beginAtZero: true
          }
        }
      }
    };

    const myChart = new Chart(
      document.getElementById('myChart'),
      config
    );
  </script>
</body>
</html>
    HTML
  end
end

main()