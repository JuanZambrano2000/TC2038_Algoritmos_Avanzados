/**
 * Actividad Ejemplos de "divide y vencerás" y algoritmos avaros
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

const vector<int> rodPrices = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};

int cut(const vector<int> &prices, int length) {
  if (length == 0) {
    return 0;
  }
  int maxValue = -2147483648;
  for (int i = 1; i <= length; i++) {
    int tmpPrice = (i - 1 < prices.size()) ? prices[i - 1] : 0;
    maxValue = max(maxValue, tmpPrice + cut(prices, length - i));
  }
  return maxValue;
}

int main() {
  vector<int> rodLengths = {13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                            23, 24, 25, 30};

  for (int length : rodLengths) {
    auto start = chrono::high_resolution_clock::now();
    int maxEarning = cut(rodPrices, length);
    auto stop = chrono::high_resolution_clock::now();
    auto duration =
        chrono::duration_cast<chrono::microseconds>(stop - start);

    cout << "La varilla de " << length
         << " de longitud, nos da de ganancia: " << maxEarning << endl;
    cout << "Tiempo de ejecución: " << duration.count() << " microsegundos"
         << endl;
  }

  return 0;
}
