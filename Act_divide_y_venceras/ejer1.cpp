#include <chrono>
#include <iostream>
#include <random>
#include <vector>
using std::cout;
using std::mt19937;
using std::random_device;
using std::uniform_int_distribution;
using std::vector;
/**
 * Actividad Ejemplos de "divide y vencerás" y algoritmos avaros
 * Ejercicio 1
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 24/08/2023, ultima modificacion 24/08/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */

class Algorithm {
private:
  void merge(vector<int> &A, int low, int m, int high);

public:
  void printVector(vector<int> A);
  void mergeSort(vector<int> &A, int low, int high);
};

void Algorithm::printVector(vector<int> A) {
  std::cout << "Los elementos del vector ordenado son: " << std::endl;
  for (int i = 0; i < (int)A.size(); i++) {
    std::cout << A[i] << " ";
  }
  std::cout << std::endl;
}

void Algorithm::mergeSort(vector<int> &A, int low, int high) {
  if (low < high) {
    // encontrar el punto medio
    int m = low + (high - low) / 2;
    // Ordenar dos mitades
    mergeSort(A, low, m);
    mergeSort(A, m + 1, high);
    // Fusionar ambas mitades
    merge(A, low, m, high);
  }
}

void Algorithm::merge(vector<int> &A, int low, int m, int high) {
  int i, j, k;
  int n1 = m - low + 1;
  int n2 = high - m;
  // crear los vectores auxiliares L y R
  vector<int> L(n1);
  vector<int> R(n2);
  for (i = 0; i < n1; i++)
    L[i] = A[low + i];
  for (j = 0; j < n2; j++)
    R[j] = A[m + 1 + j];
  // Fusionar los vectores auxiliares Ly R ordenados
  i = j = 0;
  k = low;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      A[k] = L[i];
      i++;
    } else {
      A[k] = R[j];
      j++;
    }
    k++;
  }
  // Copia los elementos restantes
  while (i < n1) {
    A[k] = L[i];
    i++;
    k++;
  }
  while (j < n2) {
    A[k] = R[j];
    j++;
    k++;
  }
}

int main() {
  Algorithm vec;
  vector<int> vector0 = {1, 5, 6, 4, 7, 8, 11, 3};
  vector<int> vector1 = {11, 13, 15, 9, 2, 8, 6, 20, 21, 23, 11};
  vector<int> vector2 = {2, 3, 1, 4, 5, 6, 1, 2, 8, 9, 10, 10};
  vector<int> vector3 = {56, 111, 4, 65, 3, 6, 9, 12, 84, 5, 1, 77, 3, 8, 73};
  vector<int> vector4 = {86, 22, 11, 54, 76, 33, 68, 99, 42, 5,  88, 17,
                         27, 73, 90, 51, 64, 7,  29, 58, 9,  62, 97, 20,
                         14, 3,  71, 45, 66, 24, 35, 96, 81, 69, 48};
  vector<int> vector5 = {59, 13, 80, 25, 55, 93, 36, 82, 89, 1,  38, 61,
                         70, 4,  19, 98, 46, 67, 21, 87, 15, 50, 6,  30,
                         2,  74, 18, 31, 56, 77, 23, 49, 72, 28, 16};
  vector<int> vector6 = {42, 88, 76, 61, 29, 5,  3,  47, 19, 95, 69, 81,
                         53, 27, 72, 66, 39, 9,  14, 56, 32, 62, 92, 18,
                         70, 85, 24, 13, 79, 59, 28, 51, 38, 75, 10};
  // seed for random numbers
  random_device rd;
  mt19937 rng(rd());
  // Distribution for random numbers
  uniform_int_distribution<int> dist(1, 400);
  // Creating vector
  vector<int> vector7(50);
  for (int i = 0; i < vector7.size(); ++i) {
    vector7[i] = dist(rng);
  }
  vector<int> vector8(100);
  for (int i = 0; i < vector8.size(); ++i) {
    vector8[i] = dist(rng);
  }
  vector<int> vector9(150);
  for (int i = 0; i < vector9.size(); ++i) {
    vector7[i] = dist(rng);
  }
  vector<int> vector10(200);
  for (int i = 0; i < vector10.size(); ++i) {
    vector10[i] = dist(rng);
  }
  vector<int> vector11(250);
  for (int i = 0; i < vector11.size(); ++i) {
    vector11[i] = dist(rng);
  }
  vector<int> vector12(300);
  for (int i = 0; i < vector12.size(); ++i) {
    vector12[i] = dist(rng);
  }
  vector<int> vectors[] = {vector0,  vector1,  vector2, vector3, vector4,
                           vector5,  vector6,  vector7, vector8, vector9,
                           vector10, vector11, vector12};
  for (int i = 0; i < sizeof(vectors) / sizeof(vectors[0]); ++i) {
    auto start = std::chrono::high_resolution_clock::now();

    vec.mergeSort(vectors[i], 0, vectors[i].size() - 1);
    //vec.printVector(vectors[i]); don't uncomment, just testing its working
    auto end = std::chrono::high_resolution_clock::now();
    auto duration =
        std::chrono::duration_cast<std::chrono::microseconds>(end - start);

    std::cout << "Time taken for vector " << i << ": " << duration.count()
              << " microseconds with " <<vectors[i].size() << " elements" << std::endl;
  }
  
  return 0;
}
