# print(states)
states={
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

for state, abbr in tuple(states.items()):
    print(f"state is {state} abbrevation is {abbr}")