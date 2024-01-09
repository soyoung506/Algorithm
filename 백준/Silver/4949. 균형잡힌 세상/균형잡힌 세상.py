import sys


pair = {
    ')': '(',
    ']': '['
}
opener = "(["
closer = ")]"

while True:
    string = sys.stdin.readline().rstrip('\n')
    openList = []
    if string == '.':
        break
    else:
        for char in string:
            if char in opener:
                openList.append(char)
            elif char in closer:
                if not openList:
                    print("no")
                    break
                lastOpener = openList.pop()
                if pair[char] != lastOpener:
                    print("no")
                    break
        else:
            if not openList:
                print("yes")
            else:
                print("no")
