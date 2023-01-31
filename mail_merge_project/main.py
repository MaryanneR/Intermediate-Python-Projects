# Get names of people to invite and strip away unnecessary characters/spaces
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

# Get letter
with open("./Input/Letters/starting_letter.txt") as template:
    letter = template.read()

# Personalize letters and move to ReadyToSend folder
for name in name_list:
    stripped_name = name.strip("\n")
    personalized_letter = letter.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as to_send:
        to_send.write(personalized_letter)
