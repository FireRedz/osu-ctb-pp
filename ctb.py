import math

def ctb(star, ar, combo, acc, miss=0, player_combo=None):
    # Based on Pakachan's ctb pp calculator
    ar = 11 if ar > 11 else ar
    player_combo = combo if player_combo is None else player_combo

    # Conversion from Star rating to pp
    final = pow(((5*(star)/0.0049)-4),2)/100000

    # Length Bonus
    secbonus = math.log10(combo/2500.0)*0.475 if combo > 2500 else 0.0
    lengthbonus = (0.95 + 0.3 * min(1.0, combo/2500.0) + secbonus)

    final *= lengthbonus

    # Miss Penalty
    final *= pow(0.97, miss)

    # Not fc combo penalty
    final *= pow(combo/player_combo, 0.8)

    # Ar Bonus
    arbonus = 1
    if ar > 9:
        arbonus += 0.1*(ar-9.0)
    elif ar > 10:
        arbonus += 0.1*(ar-10.0)
    elif ar < 8:
        arbonus += 0.025 * (8.0-ar)

    final *= arbonus

    # Hidden bonus (wtf)
    hiddenbonus = 1
    if ar > 10:
        hiddenbonus = 1.01 + 0.04 * (11- min(11, ar))
    else:
        hiddenbonus = 1.05 + 0.075 * (10-ar)
    
    final *= pow(acc/100,5.5)

    return final
