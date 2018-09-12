# A brief description of the project
# 9/12/2018
# CTI-110 P2HW2- Male Female Percentage
# Jack Tercheria
#
# Ask the user how many males there are
# Ask the user how many females there are
# Divide the number of males by the total class number
# Divide the number of females by the total class number
# Display the percentage of males and females in the class
#
# Ask the user how many males there are
male_value = input('How many males? ')
males = int(male_value)
# Ask the user how many females there are
female_value = input('How many females? ')
females = int(female_value)
# Divide the number of males by the total class number
M = males/20
# Divide the number of females by the total class number
F = females/20
# Display the percentage of males and females in the class
print(format(M, '.0%'))
print(format(F, '.0%'))

