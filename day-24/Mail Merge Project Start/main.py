# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    names = list(map(str.strip, names))


with open("./Input/Letters/starting_letter.txt") as letters:
    letter_contents = letters.read()
    print(letter_contents)

for name in names:
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.writelines(new_letter)




# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
