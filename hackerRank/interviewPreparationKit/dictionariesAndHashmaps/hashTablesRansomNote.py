"""
Problem link
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

test case 1

6 5
two times three is not four
two times two is four


-----------------------------------------------------------------
# below solution times out for few test cases but works correctly on other test cases.

def checkMagazine(magazine, note):
    for i in note:
        if i in magazine:
            magazine.remove(i)
        else:
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))

"""


def checkMagazine(magazine, note):
    magazine_word_count = {}

    for i in magazine:
        if i in magazine_word_count:
            magazine_word_count[i] += 1
        else:
            magazine_word_count[i] = 1

    for j in note:
        if j in magazine_word_count:
            if magazine_word_count[j] > 0:
                magazine_word_count[j] -= 1
            else:
                return 'No'
        else:
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
