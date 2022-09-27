#!/usr/bin/python
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        n_turple = (lent, None)
    else:
        n_turple = (lent, sentence[0])
    return n_turple
