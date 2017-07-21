import pickle
import numpy as np

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

def initialize():
    return load_obj('protVec')

def split(start, model, seq, lis):
    for index in xrange(start,len(seq) - 2,3):
        kmer = seq[index:index+3].encode('utf-8')
        if kmer in model:
            lis.append(np.array(model[kmer]))
        else:
            lis.append(np.array(model['<unk>']))
    lis = np.mean(lis, axis=0).tolist()
    return lis   

def embedding(model, seq):
    first, second, third = [], [] , []
    #First Split
    first = split(0, model, seq, first)
    #Second Split
    second = split(1, model, seq, second)
    #Third Split
    third = split(2, model, seq, third)
    return first, second, third