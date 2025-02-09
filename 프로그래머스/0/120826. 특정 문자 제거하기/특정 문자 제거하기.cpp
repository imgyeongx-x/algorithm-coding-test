#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    
    while (my_string.find(letter) != string::npos){
        my_string = my_string.replace(my_string.find(letter), letter.size(), "");
    }
    
    answer = my_string;
    return answer;
}