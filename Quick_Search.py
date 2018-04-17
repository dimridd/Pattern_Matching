#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:34:08 2018

@author: divyanshu
"""

#%%

table = [0]*256
rest = []
def bc1(pat, m):
	for i in range(m):
		table[ord(pat[i])-65] = m-i;
	
	rest = str(set(sigma) - set(pat))
	for i in range(len(rest)):
		table[ord(rest[i])-65] = m+1;
	return table	
		
pat = "ABC"
sigma = "ABCD"
text = "ABCABCABC"
match = 0
bc = bc1(pat.upper(), len(pat))	

def QS(pat, text, m, n1):
	global match
	start = 0
	x = 0	
	j = 0
	y = 0
	
	bc = bc1(pat.upper(), m)
	while j <=  n1 - m:
		
		if pat[y] == text[x]:
			x += 1
			y += 1
			if abs(start-x) == m:
				match += 1
				j += 3
				print(j)
			else:
				continue
		else:
			j += bc[ord(text[j+m])-65]
			
		x = j
		start = j
		y = 0
		  
	return j

n1=len(text)
m=len(pat)		
(QS(pat,text, len(pat), len(text) ))
