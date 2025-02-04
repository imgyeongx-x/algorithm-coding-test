
#include <iostream>
#include <stack>
using namespace std;

int main() {

	int N;
	cin >> N;
	
	int* seq = new int[N];
	int* res = new int[N];
	stack<int> st;

	for (int i = 0; i < N; i++) {
		cin >> seq[i];
	}

	for (int i = N - 1; i >= 0; i--) {
		while (!st.empty() && seq[i] >= st.top()) {
			st.pop();
		}

		if (st.empty()) {
			res[i] = -1;
		}
		else {
			res[i] = st.top();
		}

		st.push(seq[i]);
	}

	for (int i = 0; i < N; i++) {
		cout << res[i];
		if (i != N - 1)
			cout << " ";
	}

	return 0;
}