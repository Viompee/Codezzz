# --- THE GIVENS ---
# We start with a raw string variable that has extra spaces at the ends.
raw_message = "   From: chadgpt@gemini.com To: mario@piattos.net Subject: Hello   "

# 1. String Library Methods: Stripping Whitespace
# The strip() method removes whitespace from the beginning and end of a string.
clean_message = raw_message.strip()
print("1. Cleaned Message:", clean_message)

# 2. String Library Methods: Lowercase
# The lower() method makes all characters lowercase.
# This is useful for searching because string comparisons are case-sensitive.
lower_message = clean_message.lower()
print("2. Lowercase Message:", lower_message)

# 3. Looking Inside Strings (Indexing)
# We can get a single character using an index in square brackets (starting at 0).
first_char = clean_message[0]
print("3. First character of the clean message:", first_char)

# 4. String Length
# The len() function tells us how many characters are in the string.
message_length = len(clean_message)
print("4. Total characters in the message:", message_length)

# 5. Using 'in' as a Logical Operator
# We can check if a substring exists within our string. It returns True or False.
has_gemini = "gemini" in lower_message
print("5. Does the message contain 'gemini'?", has_gemini)

# 6. Checking Prefixes
# startswith() checks if a string starts with a specific substring.
is_from = clean_message.startswith("From:")
print("6. Does the message start with 'From:'?", is_from)

# 7. Parsing and Extracting Data (find method)
# The find() method searches for a substring and returns its starting position (index).
# Let's find the position of the "@" symbol.
at_sign_pos = clean_message.find("@")
print("7. The '@' symbol is at index:", at_sign_pos)

# Let's extract the sender's email address by finding the boundaries.
# First, find the space immediately after "From:"
start_pos = clean_message.find(" ") + 1

# Next, find the next space after the email address
end_pos = clean_message.find(" ", start_pos)

# 8. Slicing Strings
# We use the positions we found to slice out just the email.
# The second number in a slice is "up to but not including".
sender_email = clean_message[start_pos:end_pos]
print("8. Extracted Sender Email:", sender_email)

# 9. Search and Replace
# The replace() method acts like "search and replace" in a word processor.
updated_email = sender_email.replace("chadgpt", "mario")
print("9. Replaced Email:", updated_email)

# 10. String Concatenation
# We can join strings together using the + operator.
greeting = "Hello " + updated_email + "!"
print("10. Concatenated Greeting:", greeting)

# 11. Looping Through Strings
# We can use a definite 'for' loop to iterate through each character in a string.
# Let's count how many times the letter 'e' appears in our clean message.
count = 0
for letter in clean_message:
    if letter == 'e':
        count = count + 1

print("11. Number of times 'e' appears in the message:", count)