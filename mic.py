import sys

class Inf:
    def __init__(this):
        pass
    def __sub__(this, RHS):
        return this

def run_mic(prog, stack):
    A = []
    
    ptr = 0
    while ptr < len(prog):
        if prog[ptr].isdigit():
            x = ""
            while prog[ptr].isdigit():
                x += prog[ptr]
                ptr += 1
            stack.append(int(x))
            ptr -= 1
        elif prog[ptr] == 's':
            stack[-1] += 1
        elif prog[ptr] == '@':
            n = stack.pop()
            A.append(stack[-n:])
            stack = stack[:-n]
        elif prog[ptr] == 'A':
            stack += A[-1]
        elif prog[ptr] == ';':
            A.pop()
        elif prog[ptr] == 'k':
            stack.append(A[-1][stack.pop() - 1])
        elif prog[ptr] == 'I':
            stack.append(Inf())
        elif prog[ptr] == '(':
            seek = ptr + 1
            level = 1
            while level > 0:
                level += prog[seek] == '('
                level -= prog[seek] == ')'
                seek += 1
            
            loop_prog = prog[ptr+1:seek-1]

            x = stack.pop()
            i = 0
            while True:
                if i == x:
                    break
                stack = run_mic(loop_prog, stack + [i])
                t = stack.pop()
                if t == 0:
                    break
                i += 1
            stack.append(i-1)

            ptr = seek - 1
    
        ptr += 1

    return stack

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    print(run_mic(prog, []))
