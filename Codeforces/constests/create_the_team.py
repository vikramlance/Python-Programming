"""
C. Create The Teams
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
There are n programmers that you want to split into several non-empty teams. The skill of the i-th programmer is ai. You want to assemble the maximum number of teams from them. There is a restriction for each team: the number of programmers in the team multiplied by the minimum skill among all programmers in the team must be at least x.

Each programmer should belong to at most one team. Some programmers may be left without a team.

Calculate the maximum number of teams that you can assemble.

Input
The first line contains the integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains two integers n and x (1≤n≤105;1≤x≤109) — the number of programmers and the restriction of team skill respectively.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109), where ai is the skill of the i-th programmer.

The sum of n over all inputs does not exceed 105.

Output
For each test case print one integer — the maximum number of teams that you can assemble.

Example
inputCopy
3
5 10
7 11 2 9 5
11 9 7 5 2

4 8
2 4 2 3
4 3 2 2 
4 11
1 3 3 7
outputCopy
2
1
0

----

Input
1000
2 839020818
455326647 226571364
1 447153477
348243555
5 229512809
389059602 452143603 504391088 899957321 406458250
5 183290958
951094047 984303365 184598276 983490715 368264840
5 939304417
140076102 779852232 689093813 980307803 106859902
2 807857259
386876697 987851130
1 525727273
587992488
6 752855611
894641945 504829176 684400293 959150520 36071083 696683229
4 497956209
253058834 462343567 916442814 846394625
2 373116458
914667828 63139622
6 982402351
441239295 690619970 4810...
Output
0
0
2
2
1
0
0
2
2
0
2
2
2
1
0
0
1
1
0
2
1
1
2
3
0
3
2
3
2
0
2
1
0
2
1
0
2
0
3
2
0
1
2
0
1
2
2
3
0
3
2
2
2
2
2
0
2
2
2
1
1
1
2
2
1
3
1
1
0
2
0
2
3
1
3
1
1
2
3
0
1
2
2
2
0
0
0
1
1
1
2
3
1
2
1
3
1
2
1
0
0
0
2
0
2
3
1
2
2
0
2
1
3
1
0
0
2
2
2
1
2
3
2
1
1
1
0
1
1
0
2
2
0
1
1
0
0
2
2
2
2
1
1
0
1
1
1
1
1
2
2
1
1
1
1
1
2
3
1
1
1
1
0
1
3
0
3
1
0
2
1...
Answer
0
0
5
5
2
1
1
3
3
1
2
2
3
1
0
0
2
2
1
3
1
2
3
5
0
5
4
6
4
0
3
2
1
5
3
0
3
1
4
3
1
2
4
0
1
4
4
5
0
3
2
3
3
3
4
1
2
2
4
3
1
1
4
3
2
6
2
2
1
3
1
4
7
2
6
1
2
4
6
1
3
5
5
4
1
0
0
2
2
2
4
5
2
2
3
6
1
4
2
1
1
1
4
1
3
6
1
2
5
0
2
2
5
1
0
1
5
2
3
3
5
6
4
1
1
1
0
2
2
0
5
3
0
1
1
0
0
4
4
3
5
1
3
0
2
3
1
1
1
4
2
1
2
1
2
2
2
4
2
2
1
1
0
2
6
0
5
1
1
3
1...
Checker Log
wrong answer 3rd numbers differ - expected: '5', found: '2'

"""


class Solution:
    def create_the_team(self, arr, min_skill):
        count = 0
        arr.sort(reverse=True)
        curr_team = []
        for i in range(len(arr)):

            if curr_team and ((len(curr_team) + 1) * arr[i]) >= min_skill:
                # print("curr_team", curr_team)
                count += 1
                curr_team = []
            else:
                curr_team.append(arr[i])
        return count


test = Solution()

t = int(input())

for i in range(t):
    num_of_prog_and_min_skills = list(map(int, input().strip().split(' ')))

    min_skill = num_of_prog_and_min_skills[1]
    arr_prog_skills = list(map(int, input().strip().split(' ')))

    result = test.create_the_team(arr_prog_skills, min_skill)
    print(result)
