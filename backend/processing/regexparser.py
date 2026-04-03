import re
from datetime import datetime

def parser(message: str):
    #finding the amount and merchant from passed messages. ' str1\.str2? ' represents that parser will look for str1 and str1+str2 combined. ' int+ ' searches for numbers in repeat 
    amount=re.search(r'(?:Rs|INR)\.?\s?(\d+)',message)
    merchant=re.search(r'(?:at|from)\s+([A-Za-z0-9\s\-\*]+)',message)  

    #cleaning parsed data and deciding transaction type
    amount=float(amount.group(1)) if amount else 0
    merchant=merchant.group(1) if merchant else "Unknown"

    message=message.lower()
    transactiontype="Unknown"
    for word in message.split():
        if word in ["debited","spend","spent","withdrawn","paid"]:
            transactiontype="debit"
            break
        elif word in ["credited","recieved"]:
            transactiontype="credit"
            break

    print(f"Amount: {amount}")
    print(f"Merhcant: {merchant}")
    print(f"Type: {transactiontype}")

    return {
        "amount":amount,
        "merchant":merchant,
        "type":transactiontype,
        "timestamp":datetime.now()
    }

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
    parser(messages)