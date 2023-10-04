#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int substring(const string& text, const string& phrase) {
    int m = text.length();
    int n = phrase.length();
    vector<vector<int>> matriz(m,vector<int>(n, 0));
    int subLenght = 0;
    int position = 0;
    for(int i = 0;i<m;i++){
        for(int j = 0; j<n;j++){
            if(text[i] == phrase[j]){
                if(i == 0 || j == 0){
                    matriz[i][j] = 1;
                }else{
                    matriz[i][j] = matriz[i-1][j-1]+1;
                    if(matriz[i][j]>subLenght){
                        subLenght = matriz[i][j];
                        position = i;
                    }
                }
            }
        }
    }
    cout<<"Frase encontrada en el texto: "<<endl;
    for(int i = 1;i<=subLenght;i++){
        cout<<text[position-subLenght+i];
    }
    cout<<endl;
    return subLenght;
};

int main() {
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

    vector<string> phrases = {
        "andjustwherehewouldbemosthorrible",
        "mindinhispresentstate",
        "goodnewsthatGregor",
        "ThiswashowGregorreceivedhisfoodeachdaynow",
        "Oneofthelegshadbeenbadlyinjured",
        "thelittlelegshadthesolidgroundunderthem",
        "andhungontothekeyorpusheditdownagainwiththe",
        "Wasitreallynotenoughtoletoneofthetrainees",
        "againwiththewholeweightofhisbodyasneeded",
        "Ifonlyhisfatherwouldstopthatunbearablehissing"
    };

    for (const string& phrase : phrases) {
        cout << "Tamaño del Substring y la frase : " << substring(metarmophosis, phrase) << endl;
    }

    return 0;
}
