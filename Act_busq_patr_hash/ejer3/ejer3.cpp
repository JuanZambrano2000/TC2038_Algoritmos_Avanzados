/**
 * Actividad: Programación dinámica, backtracking, y ramificación y poda
 * Ejercicio 2
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 24/09/2023, ultima modificacion 27/09/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */

using namespace std;

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

vector <int> sufixArray(string sentence){
    //we append a new character to avoid garbage in output
    sentence.append("$");
    int n = sentence.length();

    //vector vacio que llenaremos con los substrings
    vector<string> vecString;


    for(int i = 0;i<n;i++){
        //substr(indice del inicio de la cadena, longitud de la cadena)
        vecString.push_back(sentence.substr(n-i-1,i+1));
    }

    sort(vecString.begin(),vecString.end());

    vector<int> respuesta(n);

    for(int i = 0;i<n;i++){
        respuesta[i] = n - vecString[i].size();
    }
    return respuesta;
}


int main(){

    string sentence = "bcdeabcedeb";
    int n = sentence.length();

    cout << "String: " << sentence << " Suffix array: " <<endl;
    vector<int> respuesta = sufixArray(sentence);

    for(int i = 0;i<=n;i++){
        cout<<respuesta[i]<<" ";
    }

    return 0;
}