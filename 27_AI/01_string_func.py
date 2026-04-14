def slugify(text: str) -> str:
    # Convert the entire string to lowercase
    # This ensures consistency (e.g., URLs usually prefer lowercase)
    text = text.lower()

    # List to store the final characters of the output
    result = []

    # Flag to track whether the previous character added was a dash
    # This helps avoid adding multiple dashes in a row (e.g., "---")
    prev_was_dash = False

    # Loop through each character in the input string
    for ch in text:
        # Check if the character is alphanumeric (a-z or 0-9)
        if ch.isalnum():
            # If valid, add it to the result
            result.append(ch)

            # Reset the dash flag because we added a valid character
            prev_was_dash = False
        else:
            # If the character is NOT alphanumeric (space or special char)
            # add a dash only if the previous character was not already a dash
            if not prev_was_dash:
                result.append('-')
                prev_was_dash = True

    # Join the list into a string and remove any leading/trailing dashes
    return ''.join(result).strip('-')

print(slugify("Hello World!"))
# Expected output: hello-world

print(slugify("This   has   multiple   spaces"))
# Expected output: this-has-multiple-spaces

print(slugify("Clean@This#String$Please"))
# Expected output: clean-this-string-please

print(slugify("  Leading and trailing spaces  "))
# Expected output: leading-and-trailing-spaces

print(slugify("Version 2.0.1 released!!!"))
# Expected output: version-2-0-1-released