def get_key_from_value(MyDict, val):
    if val in MyDict.values():
        return [key for key, value in MyDict.items() if value == val][0]
    else:
        return print("This Value is not in this list.")
