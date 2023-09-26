#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std; 
const int prime = 47;
const int largeModPrime = 1e9 + 9; //another prime num ber

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

long long pollynomialRollingHash(const string& word){
    long long hashValue = 0;
    long long power = 1;
    for(char c: word){
        hashValue = (hashValue+(c-'a'+1)*power)%largeModPrime;
        power=(power*prime)%largeModPrime;
    }
    return hashValue;
}

int main() {
    long long hashV1 = pollynomialRollingHash("ejemplo");
    long long hashV2 = pollynomialRollingHash("ejemplo");
    long long hashV3 = pollynomialRollingHash("ejempla");
    cout << hashV1 << endl;
    cout << hashV2 << endl;
    cout << hashV3 << endl;
    vector<string> words = fillVectorWithWords("test.txt");
    /*
    for (const string& word : words) {
        cout << word << endl;
    }
    */
    

    return 0;
}
