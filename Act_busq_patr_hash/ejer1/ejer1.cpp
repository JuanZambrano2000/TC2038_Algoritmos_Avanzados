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
//pseudocode from chatgpt
vector<int> buildPrefixTable(const string& pattern) {
    int m = pattern.length();
    vector<int> prefixTable(m, 0);
    int length = 0;  
    for (int i = 1; i < m;) {
        if (pattern[i] == pattern[length]) {
            length++;
            prefixTable[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = prefixTable[length - 1];
            } else {
                prefixTable[i] = 0;
                i++;
            }
        }
    }
    return prefixTable;
}

int KMP(const string& text, const string& pattern) {
    int n = text.length();
    int m = pattern.length();
    vector<int> prefixTable = buildPrefixTable(pattern);

    int count = 0;  // Count of pattern occurrences
    int i = 0;      // Index for text[]
    int j = 0;      // Index for pattern[]

    while (i < n) {
        if (pattern[j] == text[i]) {
            j++;
            i++;
        }

        if (j == m) {
            // Pattern found at index i - j
            count++;
            j = prefixTable[j - 1];
            // Uncomment to see the whole phrase
            
            int start = max(0, i - 50);
            int end = min(n - 1, i + 50);
            cout << text.substr(start, end - start + 1) << endl;
            
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = prefixTable[j - 1];
            } else {
                i++;
            }
        }
    }

    return count;
}

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
    cout<<endl;
    cout<<"Funcion Z"<<endl;
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
                //uncomment to see the phrase
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
    cout<<endl;
    cout<<"KMP"<<endl;
    for (const string& pattern : patterns) {
        auto start = high_resolution_clock::now();
        int occurencesKMP = KMP(fileContent, pattern);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop - start);
        cout << "Patron: " << pattern << ", tiempo de busqueda: " << duration.count() << " ms, numero de ocurrencias: " <<  occurencesKMP << endl;
    }
        

    return 0;
}