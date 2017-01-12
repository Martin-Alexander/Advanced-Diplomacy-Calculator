import math


delegates = int(input("Base number of Delegates (i.e., City States Excluded): "))

playersAlive = int(input("Players Alive: "))
playersDead = int(input("Players Dead: "))
cityStatesAlive = int(input("City States Alive: "))
cityStatesDead = int(input("City States Dead: "))

def delegatesRequired(playersAlive, playersDead, cityStatesAlive, cityStatesDead):
    delReq = int(round((1.443 * math.log(playersAlive + 0.5 * playersDead) + 7 + 16.023 * math.log(cityStatesAlive + 0.5 * cityStatesDead) - 13.758), 0))
    return(delReq)

totalCityStates = cityStatesAlive + cityStatesDead

for i in range(0, totalCityStates + 1): # i is equal to how many city states are alive
    for j in range(0, i + 1): # j is equal to how many city states are you ally (as opposed to alive but non ally)
        delReq = delegatesRequired(playersAlive, playersDead, i, totalCityStates - i)
        delPos = delegates + j*2
        if delPos >= delReq:
            victory = "WIN"
        else:
            victory = "NO WIN"
        print("Ally: " + str(j) + ", Non-Ally: " + str(i - j) + ", Dead: " + str(totalCityStates - i))
        print("Delegates possessed: " + str(delPos) + ", Delegates Required: " + str(delReq) + ". Victory Status: " + str(victory) + "\n")

# To do: Make it such that the program calculates all the possible game scenarios (within the paramiters defined
# by the player) and presents to the user all of those in which a dimplomatic victory is possible. Such possible
# scenarios will include 1) death of all players but two, 2) all players living (even if this must be achieved
# through rebirth), 3) the possession of all delegate granting game options excluding gifting delegates from
# non-revived civs, 4) all possible combination of city-state status (ally, non-ally, dead), and finally it will
# calculate from there the minimum ammount of World Leader elections that need to be held (with you in first of
# second place) for you to win.
#
# Another possible addition will be selecting which possible values each paramiter could take on. This would be
# useful for when only a subset of hypothetical victory scenarios are practically possible (eg.: Conquering all
# but one player would allow for a diplomatic victory, but this is so unfeasable that the clutter it would
# generate makes considering it not worth it).
#
# Another possible addition would be an option to view the question from the opposing perspective. That is, what
# can be done to make victory for another play impossible. 
