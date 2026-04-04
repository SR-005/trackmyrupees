
from regexparser import parser
from fuzzymatcher import fuzzymatch
from classifier import rulebasedclassifier

def processmessage(message: str):
    data=parser(message)

    category=rulebasedclassifier(data["merchant"])
    if not category:
        correctedmerchant=fuzzymatch(data["merchant"])
        if correctedmerchant:
            category=rulebasedclassifier(correctedmerchant)

    data["category"]=category
    print("Extracted Data: ",data)


if __name__=="__main__":
    testmessages=[
        "Rs. 500 debited from your account at Amazon",
        "Rs 1200 credited to your account",
        "INR 250 spent at Swiggy Instamart",
        "Rs.750 debited at KFC-Edappally",
        "You spent Rs. 99 at Uber*Trip",
        "Rs. 2000 withdrawn from ATM",
    ]

    for messages in testmessages:
        print(f"\nTesting: {messages}")
        processmessage(messages)