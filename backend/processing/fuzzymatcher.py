#matches merchants to known merchants (if any spelling mistakes of wierd formatings occur)
from difflib import get_close_matches

knownmerchants=["zomato","swiggy","uber","ola","amazon","flipkart"]
def fuzzymatch(merchant: str):
    merchant=merchant.lower()
    matches=get_close_matches(merchant,knownmerchants,n=1,cutoff=0.7)
    if matches:
        return matches[0]
    else:
        return None