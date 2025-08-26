#include <iostream>
using namespace std;

int main() {
    string name;
    cout << "Who are you? ";
    getline(cin, name);
    string place = "Westeros";
    cout << name << ", winter is coming. Let's conquer " << place << endl;
    return 0;
}

// written by Daenerys Targaryen
