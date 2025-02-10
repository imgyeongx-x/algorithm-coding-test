#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for (auto e : numbers){
        answer.push_back(e * 2);
    }
    return answer;
}