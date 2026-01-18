#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

string title,ch1,ch2;
vector<string> strVec;
vector<int> intVec;

void namesData();
void getData();
void buildTable();


int main() {

    namesData();
    getData();
    buildTable();
    return 0;
}

void namesData() {
    cout << "Enter a title for the data:" << endl;
    getline(cin, title);
    cout << "You entered: " << title << endl;

    cout << "Enter the column 1 header:" << endl;
    getline(cin, ch1);
    cout << "You entered: " << ch1 << endl;

    cout << "Enter the column 2 header:" << endl;
    getline(cin, ch2);
    cout << "You entered: " << ch2 << endl;
}

void getData() {
    string datapoint;
    while (true) {
        cout << "Enter a data point (-1 to stop input):" << endl;
        getline(cin, datapoint);
        if (datapoint == "-1") {
            break;
        }
        size_t pos = datapoint.find(',');
        if (pos == string::npos) {
            cout << "Error: No comma in string." << endl;
            continue;
        }
        if (datapoint.find(',', pos + 1) != string::npos) {
            cout << "Error: Too many commas in input." << endl;
            continue;
        }
        string DataString = datapoint.substr(0,pos);
        string DataIntStr = datapoint.substr(pos + 1);

        try {
            int DataInt = stoi(DataIntStr);

            cout << "Data string: " << DataString << endl;
            cout << "Data integer: " << DataInt << endl;

            strVec.push_back(DataString);
            intVec.push_back(DataInt);
        }
        catch (...) {
            cout << "Error: Comma not followed by an integer." << endl;
        }
    }
}

void buildTable() {
    cout << endl;
    cout << setw(33) << right << title << endl;

    cout << setw(20) << left << ch1 << "|"
         << setw(23) << right << ch2 << endl;

    cout << string(44, '-') << endl;

    for (size_t i = 0; i < strVec.size(); i++) {
        cout << setw(20) << left << strVec[i] << "|"
             << setw(23) << right << intVec[i] << endl;
    }

    cout << endl;

    for (size_t i = 0; i < strVec.size(); i++) {
        cout << setw(20) << right << strVec[i] << " ";
        for (int j = 0; j < intVec[i]; j++) {
            cout << "*";
        }
        cout << endl;
    }
}




