import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here
def nfl_wins(team_name):
    counter=0
    for row in nfl:
        if row[2]==team_name:
            counter +=1
    return(counter)
cowboys_wins=nfl_wins("Dallas Cowboys")
falcons_wins=nfl_wins("Atlanta Falcons")

def nfl_wins_in_a_year(team,year):
    count = 0
    for row in nfl:
        if (row[2] == team and row[0]==year):
            count = count + 1
    return count
browns_2009_wins=nfl_wins_in_a_year( "Cleveland Browns", "2009" )
eagles_2009_wins=nfl_wins_in_a_year( "Philadelphia Eagles", "2009" )

print("browns 2009 wins = %d"  %browns_2009_wins)
print("eagles 2009 wins = %d"  %eagles_2009_wins)
