#include <iostream>
#include <vector>
#include <random>
#include <ctime>

/**
 * Actividad Ejemplos de "divide y vencerás" y algoritmos avaros
 * Ejercicio 3
 * Hecho por el Alumno:
 * Juan Pablo Zambrano Barajas A01636420
 * TC2038 con el Dr. Omar Mendoza
 * Creado el 24/08/2023, ultima modificacion 24/08/2023
 * Compilar:
 *   g++ -std=c++17 -Wall -O3 *.cpp -o main
 * Ejecutar:
 *   ./main
 */

int countConflicts(const std::vector<int>& board, int row, int col) {
    int conflicts = 0;
    for (int i = 0; i < 8; ++i) {
        if (i != col && (board[i] == row || std::abs(i - col) == std::abs(board[i] - row))) {
            ++conflicts;
        }
    }
    return conflicts;
}

bool minConflicts(std::vector<int>& board) {
    std::random_device rd;
    std::mt19937 rng(rd());

    // Random initial placement of queens
    for (int col = 0; col < 8; ++col) {
        board[col] = rng() % 8;
    }

    for (int step = 0; step < 100000; ++step) {
        int conflictedCols = 0;
        // Encontrar la columna con mas conflictos
        int colWithMostConflicts = -1;
        int maxConflicts = -1;
        for (int col = 0; col < 8; ++col) {
            int conflicts = countConflicts(board, board[col], col);
            if (conflicts > maxConflicts) {
                maxConflicts = conflicts;
                colWithMostConflicts = col;
            }
        }
        // Existe una solucion
        if (maxConflicts == 0) {
            return true; 
        }
        int minConflicts = 8 + 1;
        int bestRow = -1;
        for (int row = 0; row < 8; ++row) {
            int conflicts = countConflicts(board, row, colWithMostConflicts);
            if (conflicts < minConflicts) {
                minConflicts = conflicts;
                bestRow = row;
            }
        }

        board[colWithMostConflicts] = bestRow;
    }
    // No se encontro solucion
    return false; 
}

int main() {
  // tablero 8x8 con 8 reinas
    std::vector<int> board(8); 

    srand(time(0)); 

    if (minConflicts(board)) {
        std::cout << "Solution found:" << std::endl;
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j) {
                std::cout << (board[j] == i ? "X" : ".") << " ";
            }
            std::cout << std::endl;
        }
    } else {
        std::cout << "No se encontro solucion" << std::endl;
    }

    return 0;
}
