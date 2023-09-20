#include <bits/stdc++.h>
#include <string>
using namespace std;

const int numNodes = 11;
const int numColours = 4; // Updated to 4 for Red, Green, Blue, and Grey

bool isSafe(int v, vector<vector<bool>> &graph, vector<string> &color, string c) {
  for (int i = 0; i < numNodes; i++)
    if (graph[v][i] && c == color[i])
      return false;
  return true;
}

bool graphColoringUtil(vector<vector<bool>> &graph, int m, vector<string> &color,
                       int v) {
  if (v == numNodes) {
    static int solutionCount = 0;
    cout << "Solution number: " << solutionCount << endl;
    for (int i = 0; i < numNodes; i++)
      cout << "Node: " << i+1 << ", color: " << color[i] << endl;
    cout << endl;
    solutionCount++;
    return true;
  }

  bool res = false;

  // Color names
  vector<string> colorNames = {"Red", "Green", "Blue", "Grey"};

  for (int c = 0; c < m; c++) { // Iterate through color names
    string colorName = colorNames[c];
    if (isSafe(v, graph, color, colorName)) {
      color[v] = colorName;
      res = graphColoringUtil(graph, m, color, v + 1) || res;
      color[v] = ""; // Reset color
    }
  }
  return res;
}

int main() {
  vector<vector<bool>> adjGraph = {
      {false, true, false, true, false, false, false, false, false, false,
       false},
      {true, false, true, true, true, true, false, false, false, false, false},
      {false, true, false, false, false, true, false, false, false, false,
       false},
      {true, true, false, false, true, false, true, true, false, false, false},
      {false, true, false, true, false, true, false, true, true, false, false},
      {false, true, true, false, true, false, false, false, true, false, false},
      {false, false, false, true, false, false, false, true, false, true,
       false},
      {false, false, false, true, true, false, true, false, true, true, true},
      {false, false, false, false, true, true, false, true, false, false, true},
      {false, false, false, false, false, false, true, true, false, false,
       true},
      {false, false, false, false, false, false, false, true, true, true,
       false}};
  vector<string> colour(numNodes, ""); // Initialize to empty strings
  if (!graphColoringUtil(adjGraph, numColours, colour, 0)) {
    cout << "No solution exists" << endl;
  }
  return 0;
}
