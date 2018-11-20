#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pop(stack, size, stackPointer):
    element = None
    stackPointer -= 1  # dekrementacja
    if stackPointer > size - (size + 1):
        element = stack[stackPointer]
        stack[stackPointer] = None
    else:
        print("Stack overflow!")
    return stackPointer, element


def push(stack, size, stackPointer, data):
    if stackPointer < size:
        stack[stackPointer] = data
        stackPointer += 1  # inkrementacja
    else:
        print("Stack overflow!")
    return stackPointer


def main(args):
    stack = []
    stackPointer = 0
    # size = int(input("Podaj rozmiar stosu: "))
    size = 3
    stack = [None] * size
    stackPointer = push(stack, size, stackPointer, 12)
    stackPointer, element = pop(stack, size, stackPointer)
    print(element)
    print(stack)
    print(stackPointer)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
