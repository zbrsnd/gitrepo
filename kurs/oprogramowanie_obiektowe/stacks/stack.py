#!/usr/bin/env python
# -*- coding: utf-8 -*-

stack = []  # pusta lista, zasięg globalny
stackPointer = 0  # wskaźnik wierzchołka


def pop(size):
    global stack, stackPointer
    stackPointer -= 1  # dekrementacja
    if stackPointer > size - (size + 1):
        print(stack[stackPointer])
        stack[stackPointer] = None
    else:
        print("Stack overflow!")


def push(size, data):
    global stack, stackPointer
    if stackPointer < size:
        stack[stackPointer] = data
        stackPointer += 1  # inkrementacja
    else:
        print("Stack overflow!")


def main(args):
    global stack, stackPointer
    size = int(input("Podaj rozmiar stosu: "))
    stack = [None] * size
    push(size, 2)
    push(size, 5)
    pop(size)
    push(size, 3)
    pop(size)
    print(stack)
    print(stackPointer)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
