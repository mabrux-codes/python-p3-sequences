#!/usr/bin/env python3

def print_fibonacci(length):
    sequence=[]
    if length==0:
        print(sequence)
        return
    elif length==1:
        sequence=[0]
    else:
        sequence=[0,1]
        while len(sequence)<length:
            sequence.append(sequence[-1]+sequence[-2])
    print(sequence)    