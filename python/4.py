# strings
name = "Steve"
print(name, len(name), name.replace("e", "u"))
print("1" + "1")
# [start_idx:end_idx:step]
print("name[1]", name[1])
print("name[2:]", name[2:])  # name[2:len(name)]
print("name[:2]", name[:2])  # name[0:2]
print("name[:]", name[:])  # name[0:len(name)]
print()


# Robert Frost
stanza = "The woods are lovely, dark and deep,\nBut I have promises to keep..."

stanza = """
The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep."""

print(stanza)
print()


for c in name:
    print(c, end=", ")
print()
print()
