from classes import *

global inventory
inventory = {}

# convert numStats list to int
def listToInt(num):
    s = ''.join(map(str, num))
    return int(s)

# roll artifact set, type
def artifact_roll(domain):
    sets = artifact_sets.get(domain).split(',')
    artifact_set = random.choice(sets)
    artifact_type = random.choice(artifact_types)
    return [artifact_set, artifact_type]

# roll mainstat
def mainstat_roll(artifactType):
    possible_main = mainstat_dict.get(artifactType).split(',')
    return random.choice(possible_main)

# roll 4 substats
def substats_roll():
    roll_list = []
    numStats = random.choices([3, 4], [0.8, 0.2])
    noOfStats = listToInt(numStats)
    stats_rolled = random.sample([*substats_dict.keys()], int(noOfStats))

    for stat in stats_rolled:
        roll_values = substats_dict.get(stat).split(',')
        value = random.choice(roll_values)
        roll = stat + ": " + value
        roll_list.append(roll)

    return roll_list

# generates the artifact for the respective domain
def artifact_gen(domain):
    artifact_index = len(inventory) + 1
    artifactPiece = artifact_roll(str(domain))
    mainStat = mainstat_roll(artifactPiece[1])
    mainStatValue = mainStat_upgrades.get(mainStat).split(',')[0]
    subStats = substats_roll()
    artifact = Artifact(artifactPiece[0], artifactPiece[1], mainStat, mainStatValue, subStats)

    inventory[str(artifact_index)] = artifact

    main = "Set: " + artifact.name + \
              " | Slot: " + str(artifact.slot) + \
              " | Main Stat: " + str(artifact.mainStat)

    return main + " | Subs: [" + ", ".join(artifact.subStat) + "]"
