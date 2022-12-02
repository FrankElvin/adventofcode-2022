
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

infile = open(infile, 'r')

hand_points = { "X": 1, "Y": 2, "Z": 3 }
outcome_points = { "win": 6, "draw": 3, "loss": 0 }
map_me_to_opp = { "Z": "C", "Y": "B", "X": "A" }

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.

# can be made by map of maps (see task 2)
def who_wins(opp, me):
    if opp == map_me_to_opp[me]:
        return "draw"
    else:
        if opp == 'A':
            if me == 'Y': return "win"
            else: return "loss"
        elif opp == 'B':
            if me == 'Z': return "win"
            else: return "loss"
        elif opp == 'C':
            if me == 'X': return 'win'
            else: return "loss"

total_result = 0
for line in infile.readlines():
    opp, me = line[:-1].split(' ')
    #print('Opponent:', opp, ' me:', me)
    outcome = who_wins(opp, me)
    round_result = hand_points[me] + outcome_points[outcome]
    #print("Outcome: %s, points: %d" %(outcome, round_result))
    total_result += round_result

print("Total result: %d" %(total_result))


infile.close()
