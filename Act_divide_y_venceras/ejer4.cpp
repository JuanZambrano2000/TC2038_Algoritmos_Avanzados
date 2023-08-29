/**
 * Actividad Ejemplos de "divide y vencerás" y algoritmos avaros
 * Ejercicio 4
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 24/08/2023, ultima modificacion 28/08/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */

#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

// Hice el vector global para evitar el pasar de referencias
std::vector<std::pair<int, int>> coordenadasOrdenadas = {};
// Vector donde se guardan los elementos que ya han sido comparados
std::vector<bool> wasCompared{false, false, false, false, false, false, false,
                              false, false, false, false, false, false, false,
                              false, false, false, false, false, false, false,
                              false, false, false, false, false, false, false,
                              false, false, false, false, false};
// Formula para calcular distancias entre dos puntos
double calculateDistance(int x1, int y1, int x2, int y2) {
  return std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));
};
// Encontrar el vecino cercano
int findNearest(int indexToFind,
                const std::vector<std::pair<int, int>> &coordinates) {
  int indexNN = 0;
  // la distancia actual al vecino cercano es infinito
  double distanceTo = 1000000;
  // valor temporal para comparar
  double temp = 0;
  for (int i = 0; i < coordinates.size() ; i++) {
    //evitamos realizar la comparacion en caso de que ya hayamos comparado a ese elemento
    if (wasCompared[i] == false) {
      temp = calculateDistance(coordinates[i].first, coordinates[i].second,
                               coordinates[indexNN].first,
                               coordinates[indexNN].second);
      if (temp < distanceTo) {
        indexNN = i;
        distanceTo = temp;
      }
    }
  }
  wasCompared[indexNN] = true;
  return indexNN;
}
void printVector(const std::vector<std::pair<int, int>> &vec) {
  for (const auto &pair : vec) {
    std::cout << "(" << pair.first << ", " << pair.second << ") " << std::endl;
  }
  std::cout << std::endl;
};

void nearestNeighbor(const std::vector<std::pair<int, int>> &coordinates,
                     int startIndex) {
  // empezamos el nearest neighbour a si mismo y lo pasamos al final pues el mismo sera el mas cercano, como ya fue comparado ponemos en el vector el valor a true
  int nn = startIndex;
  coordenadasOrdenadas.push_back(coordinates[startIndex]);
  wasCompared[startIndex] = true;
  // Buscamos el nuevo vecino mas cercano y lo metemos al vector de coordenadas ordenadas
  for (int i = 0; i < (int)coordinates.size() - 1; i++) {
    nn = findNearest(nn, coordinates);
    coordenadasOrdenadas.push_back(coordinates[nn]);
  };
};

int main() {
  std::vector<std::pair<int, int>> coordenadasOriginales = {
      {20, 20},   {20, 40},  {20, 160}, {30, 120},  {40, 140},  {40, 150},
      {50, 20},   {60, 40},  {60, 80},  {60, 200},  {70, 200},  {80, 150},
      {90, 170},  {90, 170}, {100, 50}, {100, 40},  {100, 130}, {100, 150},
      {110, 10},  {110, 70}, {120, 80}, {130, 70},  {130, 170}, {140, 140},
      {140, 180}, {150, 50}, {160, 20}, {170, 100}, {180, 70},  {180, 200},
      {200, 30},  {200, 70}, {200, 100}};
  int indiceAComparar = 0;
  nearestNeighbor(coordenadasOriginales, indiceAComparar);
  // std::cout <<"d: " <<coordenadasOriginales.size();
  printVector(coordenadasOrdenadas);
  return 0;
}