import re
s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = "Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

