# Example word
word = "children"

# Simple morphology rule
if word.endswith("ren"):
    root = "child"
    suffix = "ren"
else:
    root = word
    suffix = ""

print("Input Word:", word)
print("Root Word:", root)
print("Suffix:", suffix)