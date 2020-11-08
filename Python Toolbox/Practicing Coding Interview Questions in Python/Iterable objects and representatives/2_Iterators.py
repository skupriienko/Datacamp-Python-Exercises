pets = {'Harry': 'Hedwig the owl', 'Hermione': 'Crookshanks the cat', 'Ron': 'Scabbers the rat'}

it = iter(pets)

print(next(it))
print(next(it))

print(list(iter(it)))
