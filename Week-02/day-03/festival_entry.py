
# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

def security(check):
    passed = []
    watchlist = []
    security_alcohol_loot = 0
    for lines in check:
        if lines['guns'] == 0:
            if lines['alcohol'] > 0:
                security_alcohol_loot += lines['alcohol']
                lines['alcohol'] = 0
            passed += [lines]
        else:
            watchlist += [lines['name']]
        security_alcohol_loot += lines['alcohol']
    print("Not allowed: ")
    print(watchlist, "\n")
    print("Allowed: ")

    for lines in passed:
        print(lines['name'])
    print("Alcohol loot: " + str(security_alcohol_loot))
    print("\n", passed)

security(queue)