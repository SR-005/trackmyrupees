import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from backend.processing.regexparser import parser
from backend.processing.fuzzymatcher import fuzzymatch
from backend.processing.classifier import rulebasedclassifier
from backend.database import db


def processmessage(message: str):
    data=parser(message)

    category=rulebasedclassifier(data["merchant"])
    if not category:
        correctedmerchant=fuzzymatch(data["merchant"])
        if correctedmerchant:
            category=rulebasedclassifier(correctedmerchant)

    data["category"]=category
    print("Extracted Data: ",data)

    db.collection("transactions").add(data)


def main():
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


if __name__=="__main__":
    main()
