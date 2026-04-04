#this process classifies the merchants into various categories
dataset={
    "zomato":"Food",
    "swiggy":"Food",
    "uber":"Transport",
    "ola":"Transport",
    "amazon":"Shopping",
    "flipkart":"Shopping"
}

def rulebasedclassifier(merchant: str):
    merchant=merchant.lower()
    for key in dataset:
        if key in merchant:
            print(f"Classifier: {dataset[key]}")
            return dataset[key]
    return None

def expanddataset(merchant: str,catergory: str):
    return 0

if __name__ == "__main__":
    rulebasedclassifier("amazon")
