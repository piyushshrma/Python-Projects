#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void findModes(int* arr, int n) {
    vector<int> modes;
    int maxcount = 0;

    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (arr[i] == arr[j])
                count++;
        }

        if (count > maxcount) {
            maxcount = count;
            modes.clear();
            modes.push_back(arr[i]);
        } else if (count == maxcount) {
            modes.push_back(arr[i]);
        }
    }

    if (modes.size() == 1) {
        cout << "Mode is: " << modes[0];
    } else {
        cout << "Modes are: ";
        for (int mode : modes) {
            cout << mode << " ";
        }
    }
}

int main() {
    int n;
    cout << "Enter number of numbers: " << endl;
    cin >> n;
    int a[n];
    cout << "Enter values: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Mean
    float sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    cout << "\nMean is: " << sum / n;

    // Median
    sort(a, a + n);
    if (n % 2 == 0) {
        int mid1 = a[n / 2 - 1];
        int mid2 = a[n / 2];
        float median = (mid1 + mid2) / 2.0;
        cout << "\nMedian is: " << median;
    } else {
        cout << "\nMedian is: " << a[n / 2];
    }

    // Mode
    findModes(a, n);

    return 0;
}
