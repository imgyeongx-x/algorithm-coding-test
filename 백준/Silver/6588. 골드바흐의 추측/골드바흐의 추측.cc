
#include <iostream>
#include <cmath>
using namespace std;

int arr[1000001];

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(0);

	int n;
	cin >> n;


	arr[0] = 0;
	arr[1] = 0;
	for (int i = 2; i <= 1000000; i++) {
		arr[i] = i;
	}

	for (int i = 2; i <= sqrt(1000000); i++) {
		if (arr[i] == 0)
			continue;
		for (int j = i * i; j <= 1000000; j += i) {
			arr[j] = 0;
		}
	}

	while (n != 0) {
		bool check = false;

		for (int i = 3; i <= n / 2; i+=2) {
			if (arr[i] == 0)
				continue;
			if (arr[i] + arr[n - i] == n)
			{
				check = true;
				cout << n << " = " << i << " + " << n - i << "\n";
				break;
			}
		}
		
		if (check == false)
			cout << "Goldbach's conjecture is wrong." << "\n";

		check = false;
		
		cin >> n;
	}

	return 0;
}