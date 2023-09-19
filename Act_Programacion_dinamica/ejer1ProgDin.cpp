/**
 * Actividad: Programación dinámica, backtracking, y ramificación y poda
 * Ejercicio 1 - varilla dinamica
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

const vector<int> rodPrices = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};

int cut(const vector<int> &prices, int length) {
  vector<int> dp(length + 1, 0); 
  for (int i = 1; i <= length; i++) {
    int maxValue = -2147483648;
    for (int j = 1; j <= i; j++) {
      int tmpPrice = (j - 1 < prices.size()) ? prices[j - 1] : 0;
      maxValue = max(maxValue, tmpPrice + dp[i - j]);
    }
    dp[i] = maxValue; 
  }
  return dp[length];
}

int main() {
  int length = 20;
  auto start = std::chrono::high_resolution_clock::now();
  int maxEarning = cut(rodPrices, length);
  auto stop = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

  cout << "La varilla de " << length
       << " de longitud, nos da de ganancia: " << maxEarning << endl;
  cout << "Tiempo de ejecución: " << duration.count() << " microsegundos" << endl;
  return 0;
}
