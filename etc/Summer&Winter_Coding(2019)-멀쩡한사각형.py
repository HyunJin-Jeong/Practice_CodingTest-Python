from math import gcd
def solution(w,h): result = w * h - (w + h - gcd(w, h)); return result
