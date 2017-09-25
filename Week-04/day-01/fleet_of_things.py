from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch
item1 = Thing("Get milk!")
item2 = Thing("Remove the obstacles")
item3 = Thing("Stand up")
item4 = Thing("Eat lunch")


item3.complete()
item4.complete()

print(item1)
print(item2)
print(item3)
print(item4)

print(fleet)