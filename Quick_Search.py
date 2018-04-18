#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:34:08 2018

@author: divyanshu
"""

#%%
import time

table = [0]*256
rest = []
def bc1(pat, m):
	for i in range(len(table)):
		table[i] = m
	
	for i in range(m):
		pre = table[ord(pat[i])-65]
		table[ord(pat[i])-65] = m-i-1;
		if table[ord(pat[i])-65] == 0:
			table[ord(pat[i])-65] = pre
			
	return table	
		
with open('hi', 'r') as myfile:
	   data=myfile.read().replace('\n', '')
		   
pat = "MA"
sigma = "ABCDEFGHIJKLMLOPQRSTUVWXYZ"
text = data
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
		
		if j+m > n1-1:
			break;
			
		if pat[y] == text[x]:
			x += 1
			y += 1
			if abs(start-x) == m:
				match += 1
				j += 3
			else:
				continue
		else:
			
			j += bc[ord(text[j+m])-65]
			#print(ord(text[j+m]))
		x = j
		start = j
		y = 0
		  
	return match

n1=len(text)
m=len(pat)
t1 = time.time()
print ('start')
		
print(QS(pat,text, len(pat), len(text) ))

t2 = time.time()
print ( (t2 - t1) * 1000) 

