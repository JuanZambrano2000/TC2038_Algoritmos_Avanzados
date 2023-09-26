#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std; // Add this line to use the std namespace

// Function to read a text file and insert words into a vector
vector<string> fillVectorWithWords(const string& filename) {
    ifstream inputFile(filename);
    vector<string> words;

    if (!inputFile.is_open()) {
        cerr << "Error abriendo el archivo, revisa la ruta o el nombre" << endl;
        return words; // Return an empty vector in case of an error
    }

    string line;
    while (getline(inputFile, line)) {
        // Tokenize the line into words using a stringstream
        istringstream iss(line);
        string word;
        while (iss >> word) {
            words.push_back(word);
        }
    }

    inputFile.close();
    return words;
}

/*
long long pollynomialRollingHash(const string& word){

}*/

int main() {
    vector<string> words = fillVectorWithWords("test.txt");

    if (words.empty()) {
        cout << "No words found in the file." << endl;
    } else {
        cout << "Words in the file:" << endl;
        for (const string& word : words) {
            cout << word << endl;
        }
    }

    return 0;
}
