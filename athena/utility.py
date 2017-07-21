import pickle

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

def initialize():
    return load_obj('protVec')

def embedding(model, seq):
    first, second, third = [], [] , []
    #First Split
    for index in xrange(0,len(seq) - 2,3):
        print seq[index:index+3]
        first.append(seq[index:index+3])
    #Second Split
    for index in xrange(1,len(seq) - 2,3):
        print seq[index:index+3]
        second.append(seq[index:index+3])
    #Third Split
    for index in xrange(2,len(seq) - 2,3):
        print seq[index:index+3]
        third.append(seq[index:index+3])
    return first, second, third