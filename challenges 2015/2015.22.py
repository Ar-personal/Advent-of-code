import itertools
import random


bhp = 50
bdmg = 8

i = 0

# "name": "Drain", "mana": 73, "dmg": 2, "heal": 2, "armour": 0, "turns": 0, "clarity": 0
spells = [
    [53, 4, 0, 0, 0, 0],
    [73, 2, 2, 0, 0, 0],
    [113, 0, 0, 7, 6, 0],
    [173, 3, 0, 0, 6, 0],
    [229, 0, 0, 0, 5, 101]
]

manaSpent = 1e100
spellsUsed = []

def simulate():
    spellsUsed.clear()
    bhp = 55
    php = 50
    bdmg = 8
    pmana = 500
    turn = 0
    parmr = 0
    poisonTurns = 0
    shieldTurns = 0
    rechargeTurns = 0
    manaUsed = 0
    while True:
        if turn % 2 == 0:
            php -= 1
        if php <= 0:
            return manaSpent
        if poisonTurns > 0:
            bhp -= 3
            poisonTurns -= 1
        if bhp <= 0:
            return manaUsed
        if rechargeTurns > 0:
            pmana += 101
            rechargeTurns -= 1
            if pmana < 53:
                return manaSpent
        if php <= 0 or pmana < 53:
            return manaSpent
        if shieldTurns > 0:
            shieldTurns -= 1
        if shieldTurns == 0:
            parmr = 0
        if turn % 2 > 0:
            php -= max(1, bdmg - parmr)
        if turn % 2 == 0:
            while True:
                temp_spells = spells.copy()
                popped = 0
                if shieldTurns > 0:
                    temp_spells.pop(2 - popped)
                    popped +=1
                if poisonTurns > 0:
                    temp_spells.pop(3 - popped)
                    popped += 1
                if rechargeTurns > 0:
                    temp_spells.pop(4 - popped)
                    popped += 1
                spell = random.choice(temp_spells)
                spell_index = spells.index(spell)
                if spell[0] <= pmana:
                    break
            if spell_index == 0:
               # cast MM
                bhp -= max(1, spell[1])
                pmana -= spell[0]
                manaUsed += spell[0]
            elif spell_index == 1:
                # drain
                bhp -= 2
                php += 2
                pmana -= spell[0]
                manaUsed += spell[0]
            elif spell_index == 2:
                # cast shield
                if shieldTurns == 0:
                    shieldTurns = spell[4]
                    parmr = 7
                    pmana -= spell[0]
                    manaUsed += spell[0]
            elif spell_index == 3:
                #cast Poison
                if poisonTurns == 0:
                    poisonTurns = spell[4]
                    pmana -= spell[0]
                    manaUsed += spell[0]
            elif spell_index == 4:
                #cast rehcarge
                if rechargeTurns == 0:
                    rechargeTurns = spell[4]
                    pmana -= spell[0]
                    manaUsed += spell[0]
            spellsUsed.append(spell)
        turn += 1
        if bhp <= 0:
            return manaUsed


while True:
        mana = min(manaSpent, simulate())
        if mana < manaSpent:
            manaSpent = mana
            print(manaSpent
                  )
