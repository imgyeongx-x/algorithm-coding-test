#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int c = 1;
    for (auto e : s){
        if (e == '+')
            continue;
        else if (e == '-')
            c = -1;
        else {
            answer = answer * 10 + e - '0';
        }
    }
    answer *= c;
    return answer;
}