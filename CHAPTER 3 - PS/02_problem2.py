letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Smit").replace("<|Date|>", "19 February 2027"))