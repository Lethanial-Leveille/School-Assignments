#include <iostream>
using namespace std;

int main() {
    int userNum;
    int userNumb;

    cout << "Enter integer: " << endl;
    cin  >> userNum;
    cout << "You entered: " << userNum << endl;
    cout << userNum << " squared is " << userNum * userNum << endl;
    cout << "And " << userNum << "cubed is " << userNum * userNum * userNum * userNum << "!!" << endl;
    cout << "Enter another integer: " << endl;
    cin  >> userNumb;
    cout << userNum << "+" << userNumb << "is" << userNum + userNumb << endl;
    cout << userNum << "*" << userNumb << "is" << userNum * userNumb << endl;

    /* Type your code here */

    return 0;
}