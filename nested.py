#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = 'ericmhanson'

import sys

def nest_bracks(line):
    openers = ('(', '[', '<', '{', '(*')
    closers = (')', ']', '>', '}', '*)')
    stack = []
    count = 0

    while line:
        token = line[0]
        if line.startswith('(*'):
            token = '(*'
        elif line.startswith('*)'):
            token = '*)'
        count += 1
        line = line[len(token):]
        
        if token in openers:
            stack.append(token)
        elif token in closers:
            i = closers.index(token)
            expected_opener = openers[i]
            if not stack or stack.pop() != expected_opener:
                return 'No ' + str(count)
    
    if stack:
        return 'No ' + str(count)
    return 'Yes'

def main(args):
    with open(args) as document_text:
        text_str = document_text.readlines()
    with open('output.txt', 'w+') as file:
        for i in text_str:
            file.write(str(nest_bracks(i)) + '\n')
    

if __name__ == '__main__':
    main(sys.argv[1])
