/**
 * Actividad: Programación dinámica, backtracking, y ramificación y poda
 * Ejercicio 1 - varilla recursiva
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 14/09/2023, ultima modificacion 18/09/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */
#include <chrono>
#include <iostream>
#include <vector>
using namespace std;

long long maxEarning = 0;
const vector<int> rodPrices = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};

int cut(const vector<int> &prices, int lenght) {
  // Base case
  if (lenght == 0) {
    return 0;
  }
  int maxValue = -2147483648;
  long long costo = 0;
  for (int i = 1; i <= lenght; i++) {
    int tmpPrecio = 0;
    if (i - 1 < prices.size()) {
      tmpPrecio = prices[i - 1];
    }
    maxValue = max(tmpPrecio + cut(prices, lenght - i), maxValue);
  }
  return maxValue;
}

int main() {
  int length = 20;
  auto start = std::chrono::high_resolution_clock::now();
  maxEarning = cut(rodPrices, length);
  auto stop = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

  cout << "La varilla de " << length
       << " de longitud, nos da de ganancia: " << maxEarning << endl;
  cout << "Tiempo de ejecución: " << duration.count() << " microsegundos" << endl;
  return 0;
}
