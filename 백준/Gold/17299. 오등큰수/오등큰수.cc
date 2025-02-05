#include <iostream>
#include <stack>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N];
	int max = -1;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		if (max < arr[i])
			max = arr[i];
	}

	int* hashmap = new int[max + 1];
	for (int i = 0; i < max + 1; i++) {
		hashmap[i] = 0;
	}

	for (int i = 0; i < N; i++) {
		hashmap[arr[i]]++;
	}

	int* cnt = new int[N];

	for (int i = 0; i < N; i++) {
		cnt[i] = hashmap[arr[i]];
	}

	stack<int> st;
	int* res = new int[N];

	for (int i = N - 1; i >= 0; i--) {
		while (!st.empty() && cnt[i] >= hashmap[st.top()]) {
			st.pop();
		}
		if (st.empty()) {
			res[i] = -1;
		}
		else {
			res[i] = st.top();
		}
		st.push(arr[i]);
	}

	for (int i = 0; i < N; i++) {
		cout << res[i] << " ";
	}
	

}