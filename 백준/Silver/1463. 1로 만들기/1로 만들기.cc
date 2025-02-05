
#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N+1];

	arr[0] = 0;
	arr[1] = 0;

	for (int i = 2; i <= N; i++) {
		arr[i] = arr[i - 1] + 1;
		if (i % 2 == 0) {
			if (arr[i] > arr[i / 2] + 1) {
				arr[i] = arr[i / 2] + 1;
			}
		}
		if (i % 3 == 0) {
			if (arr[i] > arr[i / 3] + 1) {
				arr[i] = arr[i / 3] + 1;
			}
		}
	}

	cout << arr[N];

	return 0;
}