#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:17:00 2020

@author: borongwang
"""
print("hello world!")

age = 34
print(age)
# One year passed
age += 1
print(age)

first_name = "John"
last_name = "Lennon"

# Concatenation
sentence = "Hi, my name is "+first_name + " "+ last_name
print(sentence)

# Interpolation #f string
sentence2 = f"Hello, my name is {first_name} {last_name}"
print(sentence2)

