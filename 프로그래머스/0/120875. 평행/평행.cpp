#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> dots) {
    double slope1 = (double)(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0]);
    double slope2 = (double)(dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0]);
    
    if (slope1 == slope2)
        return 1;
    
    slope1 = (double)(dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0]);
    slope2 = (double)(dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0]);
    
    if (slope1 == slope2 && (dots[2][0] - dots[0][0]) != 0 && (dots[3][0] - dots[1][0]) != 0)
        return 1;
    
    slope1 = (double)(dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0]);
    slope2 = (double)(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0]);
    
    if (slope1 == slope2)
        return 1;
    
    return 0;
}