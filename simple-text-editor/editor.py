# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def editor():
    with open('input2', 'r') as file:
        num_ops = int(file.readline().strip())
        s = ''
        stack = []
        for i in range(num_ops):
            # print('s: ', s)
            # print('s: ', s)
            op = file.readline().split()
            if len(op) == 1:
                s = stack.pop()
            else:
                op, idx = op
                if int(op) == 1:
                    stack.append(s)
                    s += idx
                elif int(op) == 2:
                    stack.append(s)
                    new_s = ''
                    for i in range(len(s) - (int(idx))):
                        new_s += s[i]
                    s = new_s
                else:
                    print(s[int(idx) - 1])

if __name__ == '__main__':
    editor()