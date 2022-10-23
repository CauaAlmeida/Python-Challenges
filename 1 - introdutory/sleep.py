sunday = float(input('How many hours did you sleep on sunday: '))
monday = float(input('How many hours did you sleep on monday: '))
tuesday = float(input('How many hours did you sleep on tuesday: '))
wednesday = float(input('How many hours did you sleep on wednesday: '))
thursday = float(input('How many hours did you sleep on thursday: '))
friday = float(input('How many hours did you sleep on friday: '))
saturday = float(input('How many hours did you sleep on saturday: '))

average = (sunday + monday + tuesday + wednesday + thursday + friday + saturday) / 7

print(f'On the last week you\'ve slept {average} hours on average ')
