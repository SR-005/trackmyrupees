#this process classifies the merchants into various categories
dataset={
    "zomato":"Food",
    "swiggy":"Food",
    "uber":"Food",
    "ola":"Food",
    "amazon":"Food",
    "flipkart":"Food"
}

def rulebasedclassifier(merchant: str):
    merchant=merchant.lower()
    for key in dataset:
        if key in merchant:
            return dataset[key]
    return None

def expanddataset(merchant: str,catergory: str):
    return 0