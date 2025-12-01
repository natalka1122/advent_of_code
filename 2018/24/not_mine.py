import re

def binary_search(f, lo=0, hi=None):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Assert that f(lo) != f(hi).
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo+offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    best_so_far = lo if lo_bool else hi
    while lo <= hi:
        mid = (hi + lo) // 2
        result = f(mid)
        if result:
            best_so_far = mid
        if result == lo_bool:
            lo = mid + 1
        else:
            hi = mid - 1
    return best_so_far


inp = """
Immune System:
1514 units each with 8968 hit points (weak to cold) with an attack that does 57 bludgeoning damage at initiative 9
2721 units each with 6691 hit points (weak to cold) with an attack that does 22 slashing damage at initiative 15
1214 units each with 10379 hit points (immune to bludgeoning) with an attack that does 69 fire damage at initiative 16
2870 units each with 4212 hit points with an attack that does 11 radiation damage at initiative 12
1239 units each with 5405 hit points (weak to cold) with an attack that does 37 cold damage at initiative 18
4509 units each with 4004 hit points (weak to cold; immune to radiation) with an attack that does 8 slashing damage at initiative 20
3369 units each with 10672 hit points (weak to slashing) with an attack that does 29 cold damage at initiative 11
2890 units each with 11418 hit points (weak to fire; immune to bludgeoning) with an attack that does 30 cold damage at initiative 8
149 units each with 7022 hit points (weak to slashing) with an attack that does 393 radiation damage at initiative 13
2080 units each with 5786 hit points (weak to fire; immune to slashing, bludgeoning) with an attack that does 20 fire damage at initiative 7

Infection:
817 units each with 47082 hit points (immune to slashing, radiation, bludgeoning) with an attack that does 115 cold damage at initiative 3
4183 units each with 35892 hit points with an attack that does 16 bludgeoning damage at initiative 1
7006 units each with 11084 hit points with an attack that does 2 fire damage at initiative 2
4804 units each with 25411 hit points with an attack that does 10 cold damage at initiative 14
6262 units each with 28952 hit points (weak to fire) with an attack that does 7 slashing damage at initiative 10
628 units each with 32906 hit points (weak to slashing) with an attack that does 99 radiation damage at initiative 4
5239 units each with 46047 hit points (immune to fire) with an attack that does 14 bludgeoning damage at initiative 6
1173 units each with 32300 hit points (weak to cold, slashing) with an attack that does 53 bludgeoning damage at initiative 19
3712 units each with 12148 hit points (immune to cold; weak to slashing) with an attack that does 5 slashing damage at initiative 17
334 units each with 43582 hit points (weak to cold, fire) with an attack that does 260 cold damage at initiative 5""".strip()

def doit(boost=0, part1=False):
    lines = inp.splitlines()
    immune, infection = inp.split("\n\n")

    teams = []

    REGEX = re.compile(r"(\d+) units each with (\d+) hit points (\([^)]*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)")

    # namedtuple? who needs namedtuple with hacks like these?
    UNITS, HP, DAMAGE, DTYPE, FAST, IMMUNE, WEAK = range(7)

    blah = boost
    for inps in [immune, infection]:
        lines = inps.splitlines()[1:]
        team = []
        for line in lines:
            s = REGEX.match(line)
            units, hp, extra, damage, dtype, fast = s.groups()
            immune = []
            weak = []
            if extra:
                extra = extra.rstrip(" )").lstrip("(")
                for s in extra.split("; "):
                    if s.startswith("weak to "):
                        weak = s[len("weak to "):].split(", ")
                    elif s.startswith("immune to "):
                        immune = s[len("immune to "):].split(", ")
                    else:
                        assert False
            u = [int(units), int(hp), int(damage) + blah, dtype, int(fast), set(immune), set(weak)]
            team.append(u)
        teams.append(team)
        blah = 0
    
    def power(t):
        return t[UNITS] * t[DAMAGE]

    def damage(attacking, defending):
        mod = 1
        if attacking[DTYPE] in defending[IMMUNE]:
            mod = 0
        elif attacking[DTYPE] in defending[WEAK]:
            mod = 2
        return power(attacking) * mod
    
    def sort_key(attacking, defending):
        return (damage(attacking, defending), power(defending), defending[FAST])
    
    while all(not all(u[UNITS] <= 0 for u in team) for team in teams):
        teams[0].sort(key=power, reverse=True)
        teams[1].sort(key=power, reverse=True)

        targets = []

        # target selection
        for team_i in range(2):
            other_team_i = 1 - team_i
            team = teams[team_i]
            other_team = teams[other_team_i]

            remaining_targets = set(i for i in range(len(other_team)) if other_team[i][UNITS] > 0)
            my_targets = [None] * len(team)

            for i, t in enumerate(team):
                if not remaining_targets:
                    break
                best_target = max(remaining_targets, key= lambda i: sort_key(t, other_team[i]))
                enemy = other_team[best_target]
                if damage(t, enemy) == 0:
                    continue
                my_targets[i] = best_target
                remaining_targets.remove(best_target)
            targets.append(my_targets)
        
        # attacking
        attack_sequence = [(0, i) for i in range(len(teams[0]))] + [(1, i) for i in range(len(teams[1]))]
        attack_sequence.sort(key=lambda x: teams[x[0]][x[1]][FAST], reverse=True)
        did_damage = False
        for team_i, index in attack_sequence:
            to_attack = targets[team_i][index]
            if to_attack is None:
                continue
            me = teams[team_i][index]
            other = teams[1-team_i][to_attack]

            d = damage(me, other)
            d //= other[HP]

            if teams[1-team_i][to_attack][UNITS] > 0 and d > 0:
                did_damage = True

            teams[1-team_i][to_attack][UNITS] -= d
            teams[1-team_i][to_attack][UNITS] = max(teams[1-team_i][to_attack][UNITS], 0)
        if not did_damage:
            return None
    
    if part1:
        return sum(u[UNITS] for u in teams[0]) or sum(u[UNITS] for u in teams[1])
    asd = sum(u[UNITS] for u in teams[0])
    if asd == 0:
        return None
    else:
        return asd
# print(doit(part1=True))
# I did a manual binary search, submitted the right answer, then added in did_damage.
# Turns out that doit can infinite loop without the did_damage check!
# WARNING: "doit" is not guaranteed to be monotonic! You should manually check values yourself.
# print(doit(33))
maybe = binary_search(doit)
print(doit(maybe))