# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 03:13:54 2023

@author: fadel
"""
import CompleteTwitterSentiment

class socialSentiment():
    """data type for an AI that aquires posts from tiwtter among other 
    sources to determine indicators of a rise or fall"""
    def __init__(self, init_score, init_stock_tag):
        self.score = init_score
        self.stock_tag = init_stock_tag

    def __repr__(self):
        s= "Sentiment on " + self.stock_tag + " is scored " + str(self.score) + " on the index."  
        return s