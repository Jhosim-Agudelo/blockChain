import hashlib
import json
from time import time


class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        self.current_transactions = list()

    def new_block(self,proof,previous_hash=None):
        
        block = {
            'index': len(self.chain)+ 1,
            'timestamp':time(),
            'transactions':self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.current_transactions = []

        self.chain.append(block)
       
        return block


    
    def new_transaction(self,sender,recipient,amount):
        
        self.transactions.append({  'sender': sender
                                    ,'recipient':recipient
                                    ,'amount':amount                                  
                                })
        
        return self.last_block['index']+1

    @staticmethod
    def hash(block):
        # dumps converts a python object into a json formatted string, sort keys ensure keys in dict are sorted alphabetically in json result
        # .encode() encodes the JSON string into a utf 8 encoding, the sha 256 function requires bytes format
        block_string = json.dumps(block,sort_keys=True).encode()


        return hashlib.sha256(block_string).hexdigest() # creates a hash object and then converts to hexadecimal string

    @property
    def last_block(self):
        return self.chain[-1]