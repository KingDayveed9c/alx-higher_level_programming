#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        n_tuple = (lent, None)
    else:
        n_tuple = (lent, sentence[0])
    return n_tuple
