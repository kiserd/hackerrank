# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def editor():
    # use file input while working in IDE
    with open('input2', 'r') as file:
        num_ops = int(file.readline().strip())
        s = ''
        stack = []
        for i in range(num_ops):
            # get operation number and idx/string
            op = file.readline().split()
            # if only one input item, undo last action
            if len(op) == 1:
                s = stack.pop()
            else:
                op, idx = op
                # append new string to end of s
                if int(op) == 1:
                    stack.append(s)
                    s += idx
                # remove last idx characters from s
                elif int(op) == 2:
                    stack.append(s)
                    new_s = ''
                    for i in range(len(s) - (int(idx))):
                        new_s += s[i]
                    s = new_s
                # print desired character
                else:
                    print(s[int(idx) - 1])

if __name__ == '__main__':
    editor()