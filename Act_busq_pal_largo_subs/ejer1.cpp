#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

string preprocess(string text){
    string c = "|";
    string processedString = "";
    for(int i = 0; i<text.length();i++){
        c = c + text[i] + "|";
    }
    return processedString;
}
string manacher(string file){
    int center = 0;
    int left = 0;
    int right = 0;
    string palindrome = "";
    string charStringFile = preprocess(file);
    for(char c: charStringFile){
        cout<<c;
    }
    return charStringFile;
};

int main(){
    ifstream file("metamorphosis.txt");
    if(!file.is_open()){
        cerr<<"Error al abrir el archivo, revisa la ruta"<<endl;
    }
    string metarmophosis;
    string line;

    while (getline(file, line)) {
        istringstream iss(line);
        string word;
        while (iss >> word) {
            metarmophosis = metarmophosis + word;
        }
    }

    file.close();  // Close the file
    manacher(metarmophosis);
    //cout << "File content:\n" << metarmophosis << std::endl;

    return 0;  // Exit successfully
}