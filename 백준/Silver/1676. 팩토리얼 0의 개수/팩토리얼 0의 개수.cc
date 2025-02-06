
#include <iostream>

using namespace std;


int main() {

	cin.tie(NULL);
	ios_base::sync_with_stdio(0);

	int N;
	cin >> N;

	int res = N / 5 + N / 25 + N / 125;

	cout << res;

	return 0;
}