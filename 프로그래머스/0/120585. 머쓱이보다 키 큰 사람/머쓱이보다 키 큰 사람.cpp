#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int height) {
    sort(array.begin(), array.end());
    int answer = 0;
    for (answer = 0; answer < array.size(); answer++){
        if (array[answer] > height)
            break;
    }
    answer = array.size() - answer;
    return answer;
}