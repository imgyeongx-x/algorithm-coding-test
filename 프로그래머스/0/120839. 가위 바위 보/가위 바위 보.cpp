#include <string>
#include <vector>

using namespace std;

string solution(string rsp) {
    string answer = "";
    
    for (auto e : rsp){
        if (e == '2')
            answer.push_back('0');
        if (e == '0')
            answer.push_back('5');
        if (e == '5')
            answer.push_back('2');
    }
    
    return answer;
}