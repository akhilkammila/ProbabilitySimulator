"""
n-card bomb pot

What I want to know
- chance of making diff combinations within hand (5 out of own n)
- on random flop, turn, river, chances of combos

Motivation:
- lost $100 on full house over full house in hand
- turns out 9-card hand, full house+ is 12%, higher than i thought (https://www.durangobill.com/Poker_Probabilities_8_Cards.html)
- 2 full houses+/5 people = 10% chance

Other
- need to consider whether someone is betting bc of their in-hand on board hand
- was easy fold (they were def betting becasue of in-hand)
"""



"""
On Board

9 cards (max for 5 people)
- 12% chance of fh
- max of 5 people
--> 49% chance of 1+ full house
--> 1 full house: 5c1 * (.12)(.88^4) = 36%
--> 2 full house: 5c2 * (.12^2)(.88^3) = 10% (full house over full house p likely)

10 cards (not max for 4 ppl, can go 11)
- 19% cahnce of fh
- max of 4 people
--> 57% chance of 1+ full house
--> 1 full house: 4c1 * (.19)(.81^3) = 40%
--> 2 full house: 4c2 * (.19^2)(.81^2) = 14%
--> 3 full house: 4c3 * (.19^3)(.81^1) = 2%
"""