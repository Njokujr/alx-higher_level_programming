#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        sent_len = len(sentence)
        if sent_len == 0:
            return (sent_len, None)
        return (sent_len, sentence[0])
