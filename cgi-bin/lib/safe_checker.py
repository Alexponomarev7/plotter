#! /usr/bin/env python3

safe_tokens = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '+', '-', '*', '/',
                '(', ')', '[', ']', 
                'sin', 'cos', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg', 'f', 'pi', 'x', 'sgn',
                ' ']

class SafetyException(Exception):
    pass

def check(expr):
    for token in safe_tokens:
        expr = expr.replace(token, '')
    if len(expr) != 0:
        raise SafetyException()

