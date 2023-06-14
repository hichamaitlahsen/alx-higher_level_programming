#!/usr/bin/python3
def multiply_by_2(aDictionary):
    dirictor= aDictionary.copy()
    list_keys = list(dirictor.keys())

    for i in list_keys:
        dirictor[i] *= 2

    return (dirictor)
