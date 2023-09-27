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

using namespace std;

vector<int> funcionZ(string text){
    
    int n = text.length();
    vector<int> vectorZ(n,0);


    for(int i = 1, l = 0, r = 0; i<n;i++){
        if(i <= r){
            vectorZ[i] = min(r-i+1, vectorZ[i-l]);
        }
        while(i + vectorZ[i] < n && text[vectorZ[i]] == text[i+vectorZ[i]]){
            vectorZ[i] = vectorZ[i]+1;
        }
        if(i+vectorZ[i] - 1  > r){
            l = i;
            r = i + vectorZ[i] - 1;
        }
    }

    return vectorZ;
}

int main(){

    ifstream file("test.txt");
    if (!file.is_open()) {
        cerr << "Error abriendo el archivo, revisa la ruta o el nombre" << endl;
    }

    string line;
    string fileContent;

    while (getline(file, line)) {
        fileContent += line;
    }
    file.close();

    vector<string> patterns = {"not", "adios", "the", "it", "hola"};

    for (const string& pattern : patterns) {
        string text = pattern + "*" + fileContent;

        int n = fileContent.length();
        vector<int> vectorZ = funcionZ(text);

        for (int i = 0; i < n; i++) {
            if (vectorZ[i] == pattern.length()) {
                for (int y = 0; y < 50; y++) {
                    cout << text[i + y];
                }
                cout << endl;
                cout << endl;
            }
        }
    }
    return 0;
};