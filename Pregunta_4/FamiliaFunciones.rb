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

  def recursion_cola_aux(n, dicResult)
    if dicResult.key?(n)
      return dicResult[n]
    else
      dicResult[n] = recursion_cola_aux(n - 7, dicResult) + recursion_cola_aux(n - 14, dicResult) + recursion_cola_aux(n - 21, dicResult) + recursion_cola_aux(n - 28, dicResult) + recursion_cola_aux(n - 35, dicResult) + recursion_cola_aux(n - 42, dicResult) + recursion_cola_aux(n - 49, dicResult)
      return dicResult[n]
    end
  end

  return recursion_cola_aux(n, dicResult)
end

def main()
  values = [25, 50, 75, 100, 125]
  results = []

  values.each do |n|
    iterativo_time = Benchmark.realtime { iterativo(n) }
    recursivo_time = Benchmark.realtime { recursion(n) }
    recursivo_cola_time = Benchmark.realtime { recursion_cola(n) }

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