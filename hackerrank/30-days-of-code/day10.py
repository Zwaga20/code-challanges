#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    binary_n = format(n, 'b')
    con_one = binary_n.split('0')
    max_entity = max(len(group) for group in con_one)
    print(max_entity)
