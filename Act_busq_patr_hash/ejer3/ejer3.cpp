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

    //empty vector to save suffixes 
    vector<string> vecSufix;

    for(int i = 0;i<n;i++){
        vecSufix.push_back(sentence.substr(n-i-1,i+1));
    }
    // Sort the suffixes lexicographically
    sort(vecSufix.begin(),vecSufix.end());

    vector<int> sufixArray(n);

    for(int i = 0;i<n;i++){
        sufixArray[i] = n - vecSufix[i].size();
    }
    return sufixArray;
}


int main() {
    vector<string> sentences = {
        "The vaulty heaven so high above our heads.",
        "Some say the lark and loathed toad change eyes.",
        "Your lady mother is coming to your chamber.",
        "I am too young, I pray you pardon me",
        "My husband is on earth, my faith in heaven."
    };

    for (const string& sentence : sentences) {
        int n = sentence.length();
        cout << "Sentence: " << sentence << endl;
        cout << "Suffix array:" << endl;
        vector<int> sufixAnswer = sufixArray(sentence);

        for (int i = 0; i < n; i++) {
            cout << sufixAnswer[i] << " ";
        }
        cout << endl << endl;
    }

    return 0;
}
