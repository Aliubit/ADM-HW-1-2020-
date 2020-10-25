# Insertion Sort - Part 2


import math
import os
import random
import re
import sys

def insertionSort(ar):
    for q in range(1,len(ar)):
        for i in range(q):
            if(ar[q] < ar[i]):
                temp=ar[q]
                ar[q]=ar[i]
                ar[i]=temp
        print(' '.join(str(x) for x in ar))

m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
