#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    ifstream file("metamorphosis.txt");
    if(!file.is_open()){
        cerr<<"Error al abrir el archivo, revisa la ruta"<<endl;
    }
    string metarmophosis;
    string line;

    while (std::getline(file, line)) {
        metarmophosis += line + "\n";  // Append each line to the content string
    }

    file.close();  // Close the file

    std::cout << "File content:\n" << metarmophosis << std::endl;

    return 0;  // Exit successfully
}