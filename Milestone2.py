# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:24:03 2022

@author: Jack
"""

import math
def random_genome(dna, gc_content):
    print(len(dna))

    gc_counted = 0 
    for letter in dna:
        if letter == "C":
            gc_counted = gc_counted + 1
        if letter == "G":
            gc_counted = gc_counted + 1
    
    print (gc_counted)
    gc_ratio_gotten = gc_counted/len(dna)
    print (gc_ratio_gotten)
    gc_got_content = gc_ratio_gotten#/2
    print (gc_got_content)
    probs_list = []
    
    for contt in gc_content:
        fer_let_same = []
        for let in dna:
            if let == "C":
                fer_let_same.append(contt/2)
            if let == "G":
                fer_let_same.append(contt/2)
            if let == "A":
                fer_let_same.append((1-contt)/2)
            if let == "T":
                fer_let_same.append((1-contt)/2)
        
        print (str(contt) + "gcgiveen")
        prod = 1
        for numm in fer_let_same:
            prod = prod*numm
        prob_same_sing = prod
        print (str(prob_same_sing) + "probsame sing")
        #prob_same = prob_same_sing**len(dna)
        #print (prob_same)
        log_prob_same = math.log(prob_same_sing,10)
        probs_list.append(log_prob_same)
        print (probs_list)
    return probs_list
    #raw_prob = gc_got_content**len(dna)
    #print (raw_prob)
    #log_fin = math.log(raw_prob,10)
    #return (log_fin)
print (random_genome("ACGATACAA", [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]))