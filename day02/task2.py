
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
# X for Rock, Y for Paper, and Z for Scissors. (my hand)

# X for lose, Y for draw,  and Z for win
outcome_from_code = {"X": 'loss', 'Y': 'draw', 'Z': 'win'}

hand_by_outcome = {
    'win':  { "A": "Y", "B": "Z", "C": "X" },
    'loss':  { "A": "Z", "B": "X", "C": "Y" },
    'draw':  { "A": "X", "B": "Y", "C": "Z" }
}

total_result = 0
for line in infile.readlines():
    opp, outcome = line[:-1].split(' ')
    outcome = outcome_from_code[outcome]

    my_hand = hand_by_outcome[outcome][opp]
    #print("For", opp, "Need hand:", my_hand)

    round_result = hand_points[my_hand] + outcome_points[outcome]
    total_result += round_result

print("Total result: %d" %(total_result))


infile.close()
