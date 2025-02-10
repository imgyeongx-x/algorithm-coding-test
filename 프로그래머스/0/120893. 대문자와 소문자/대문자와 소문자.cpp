#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for (auto e : my_string) {
        if (e >= 'a' && e <= 'z')
            answer.push_back(e-'a'+'A');
        if (e >= 'A' && e <= 'Z')
            answer.push_back(e-'A'+'a');
    }
    return answer;
}