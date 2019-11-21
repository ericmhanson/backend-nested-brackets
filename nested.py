#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Your Github Username"

import sys

def nest_bracks(line):
    openers = ('(', '[', '<', '{', '(*')
    closers = (')', ']', '>', '}', '*)')
    stack = []
    index = 0

    while line:
        token = line[0]
        if line.startswith('(*'):
            token = '(*'
        elif line.startswith('*)'):
            token = '*)'
        
        if token in openers:
            stack.append(token)
        elif token in closers:
            if stack[-1] == openers[closers.index(token)]:
                stack.pop()
            else:
                return 'No ' + str(index)
        line = line[len(token):]
        index += 1

    if len(stack) == 0:
        return 'Yes'

def main(args):
    with open(args) as document_text:
        text_str = document_text.readlines()
    with open('output.txt', 'w+') as file:
        for i in text_str:
            file.write(str(nest_bracks(i)) + '\n')
    

if __name__ == '__main__':
    main(sys.argv[1])
