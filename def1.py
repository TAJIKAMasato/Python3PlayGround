def sayhello():
    return "こんにちは"

def postTaxPrice(price):
    ans = price * 1.08
    return ans

print(sayhello(),postTaxPrice(130),"です。")
