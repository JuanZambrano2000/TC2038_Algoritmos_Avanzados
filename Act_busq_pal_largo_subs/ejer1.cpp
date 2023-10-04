using namespace std;

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

string preprocessString(const string& text) {
    string T = "|";
    
    for (int i = 0; i < text.length(); i++) {
        T = T + text[i] + "|";
    }
    
    return T;
}

string manacher(string text){
    //Centro del palodromo más a la derecha, la derecha del palindromo más a la derecha, y a la izquierda
    int center = 0, right = 0;
    int rl = 1, m = 0, pl = 0, j = 0;

    string T = preprocessString(text);
    string palindromo = "";
    string ans = "";

    for(int i = 0; i<text.length();i++){
        T = T + text[i] + "|";
    }
    int N = T.length();
    vector<int> palindromes(N,0);
    for(int i = 0;i < N;i++){

        if(i < right){
            j = 2 * center - i;
            palindromes[i] = min(right - i, palindromes[j]);
            
        }
        rl = palindromes[i]+1;
        while(tolower(T[i-rl]) == tolower(T[i+rl]) && i-rl>=0 && i+rl<N ){
            palindromes[i]++;
            rl++;
        }
        if(palindromes[i] > m){
            pl = i;
            m = palindromes[i];
        }
        if(i + palindromes[i] > right){
            right = i + palindromes[i];
            center = i;
        }   
    }
    for(int i = 0;i<m*2+1;i++){
        if ( T[pl-m+i] != '|')
            ans += T[pl-m+i];
    }
    return ans;
}

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

    file.close();  
    cout<<manacher(metarmophosis)<<endl;

    return 0;  
}