#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cctype> 
#include <map>
#include <algorithm>

using namespace std;

const int prime = 97;
const long long largeModPrime = 1e9 + 9; //another prime num ber

long long pollynomialRollingHash(string& word){
    long long hashValue = 0;
    long long power = 1;
    for(char c: word){
        hashValue = (hashValue+(c-'a'+29)*power)%largeModPrime;
        power=(power*prime)%largeModPrime;
    }
    return hashValue;
}

map<long long, pair<string, int>> countOccurrences(vector<string>& words){
    map<long long, pair<string, int>> wordOcurrences;
    for(string& word: words){
        long long hash = pollynomialRollingHash(word);
        if(wordOcurrences.find(hash) != wordOcurrences.end()){
            wordOcurrences[hash].second++;
        }else{
            wordOcurrences[hash] = make_pair(word, 1);
        }
    }
    return wordOcurrences;
}
bool isAlphaCharacter(char c) {
    return isalpha(static_cast<unsigned char>(c));
}

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
        istringstream iss(line);
        string word;
        while (iss >> word) {
            // Process the word to keep only alphabetic characters
            string cleanedWord;
            for (char c : word) {
                if (isAlphaCharacter(c)) {
                    cleanedWord.push_back(c);
                }
            }
            if (!cleanedWord.empty()) {
                words.push_back(cleanedWord);
            }
        }
    }

    inputFile.close();
    return words;
}

int main() {
    /*
    long long hashV1 = pollynomialRollingHash("ejemplo");
    long long hashV2 = pollynomialRollingHash("ejemplo");
    long long hashV3 = pollynomialRollingHash("ejempla");
    cout << hashV1 << endl;
    cout << hashV2 << endl;
    cout << hashV3 << endl;
    */
    vector<string> words = fillVectorWithWords("romeo_and_juliet.txt");
    /*
    for (string& word : words) {
        cout << word << endl;
    }
    */
    map<long long, pair<string, int>> wo = countOccurrences(words);
    
    vector<pair<long long, pair<string, int>>> orderedOccurrences(wo.begin(), wo.end());

    // Ordenar el vector en función del valor del numero
    sort(orderedOccurrences.begin(), orderedOccurrences.end(), [](const auto& a, const auto& b) {
        return a.second.second > b.second.second; // Ordenar
    });
    int numberIteration = 1;
    for (auto& entry : orderedOccurrences) {
        long long hash = entry.first;
        string word = entry.second.first;
        int count = entry.second.second;

        cout << numberIteration <<". Hash: " << hash << ", Word: " << word << ", Count: " << count << endl;
        numberIteration++;
        if(numberIteration>=21){
            break;
        }
    }
    return 0;
}
