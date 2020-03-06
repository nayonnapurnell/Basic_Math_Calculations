# Step 1
# Ask the user for their name and the year they were born.
name = input("What is your name?")
yearOfBirth = int(input("What year were you born?"))

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
ageAt25 = int(25 + yearOfBirth)
ageAt50 = int(50 + yearOfBirth)
ageAt75 = int(75 + yearOfBirth)
ageAt100 = int(100 + yearOfBirth)

# Step 3
# If they're already past any of these ages, skip them.
