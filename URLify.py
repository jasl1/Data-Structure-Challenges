def URLify(string, true_length):
    # Convert the string to a list of characters
    string = list(string)

    # Initialize an index for the end of the string after URLification
    end = len(string)

    # Iterate through the string in reverse order
    for i in range(true_length - 1, -1, -1):
        # If the character is a space, replace it with '%20'
        if string[i] == ' ':
            string[end - 3:end] = '%20'
            end -= 3
        else:
            # If the character is not a space, copy it to the end of the string after URLification
            string[end - 1] = string[i]
            end -= 1

    # Convert the list of characters back to a string and return it
    return ''.join(string)

# Example usage:
string = "Mr John Smith    "  # Note: There are extra spaces at the end to accommodate additional characters
true_length = 13  # The true length of the string excluding the extra spaces
print(URLify(string, true_length))  # Output: "Mr%20John%20Smith"
