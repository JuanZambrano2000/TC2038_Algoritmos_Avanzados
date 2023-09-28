/**
 * Actividad: Programación dinámica, backtracking, y ramificación y poda
 * Ejercicio 1
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 24/09/2023, ultima modificacion 26/09/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */
#include <iostream>

#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<int> zFunction(string text){
    
    int n = text.length();
    vector<int> zVector(n,0);


    for(int i = 1, l = 0, r = 0; i<n;i++){
        if(i <= r){
            zVector[i] = min(r-i+1, zVector[i-l]);
        }
        while(i + zVector[i] < n && text[zVector[i]] == text[i+zVector[i]]){
            zVector[i] = zVector[i]+1;
        }
        if(i+zVector[i] - 1  > r){
            l = i;
            r = i + zVector[i] - 1;
        }
    }

    return zVector;
}

int main() {
    ifstream file("romeo_and_juliet.txt");
    if (!file.is_open()) {
        cerr << "Error abriendo el archivo, revisa la ruta o el nombre" << endl;
    }

    string line;
    string fileContent;

    while (getline(file, line)) {
        fileContent += line;
    }
    file.close();

    vector<string> patterns = {"ROMEO", "JULIET", "NURSE", "CAPULET", "hola"};

    for (const string& pattern : patterns) {
        string text = pattern + "*" + fileContent;
        int n = fileContent.length();
        // Measure the time for the search
        auto start = high_resolution_clock::now();
        vector<int> vectorZ = zFunction(text);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop - start);

        int patternCount = 0;

        for (int i = 0; i < n; i++) {
            if (vectorZ[i] == pattern.length()) {
                patternCount++;
                /*
                for (int y = 0; y < 50; y++) {
                    cout << text[i + y];
                }
                cout << endl;
                */
            }
        }
        cout << "Patron: " << pattern << ", tiempo de busqueda: " << duration.count() << " ms, numero de ocurrencias: " << patternCount << endl;
    }
    return 0;
}