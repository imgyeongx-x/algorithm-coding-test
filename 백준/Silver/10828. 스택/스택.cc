#include <iostream>
//#include <string>

using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[10000];
	int index = 0;

	for (int i = 0; i < N; i++) {
		string order;
		cin >> order;

		if (order == "push") {
			int num;
			cin >> num;
			
			arr[index] = num;
			index++;
		}

		else if (order == "pop") {
			if (index == 0)
			{
				cout << -1 << endl;
				continue;
			}
			cout << arr[index - 1] << endl;
			index--;
		}
		
		else if (order == "size") {
			cout << index << endl;
		}

		else if (order == "empty") {
			if (index == 0)
				cout << 1 << endl;
			else
				cout << 0 << endl;
		}
		
		else if (order == "top") {
			if (index == 0)
			{
				cout << -1 << endl;
				continue;
			}

			cout << arr[index - 1] << endl;
		}

		else if (order == "p") {
			for (int j = 0; j < index; j++) {
				cout << arr[j] << endl;
			}
		}
	}

	return 0;
}