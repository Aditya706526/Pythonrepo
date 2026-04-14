import re
text = "The quick brown fox jumps over the lazy dog and the fox."

match = re.search("brown", text)
print(match)
if match:
    print("Matched!~")
    print("Start index:", match.start())
    print("Start index:", match.end())

# -----------------------------------------------------------------------

matches = re.findall("the", text, re.IGNORECASE)
print("matches are:", matches)

new_text = re.sub("fox", "lion", text)
print("New text:", new_text)