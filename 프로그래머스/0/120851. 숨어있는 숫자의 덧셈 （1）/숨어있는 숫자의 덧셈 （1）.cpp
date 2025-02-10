#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for (auto e : my_string){
        if (e >= '0' && e <= '9')
            answer += e - '0';
    }
    return answer;
}