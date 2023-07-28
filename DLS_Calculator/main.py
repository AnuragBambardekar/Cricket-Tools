print("Duckworth-Lewis-Stern Calculator for ODI regulations(50 overs/innings) (min. 20 overs/side)")

"""
overs/innings must be less than 100 and must be a whole number
"""
while True:
    try:
        initial_overs = int(input("Overs at the start of the Team 1's innings [not more than 50 overs]: "))
        if 19 < initial_overs < 100:
            break
        else:
            print("Invalid input. Please enter a value between 20 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


team1_final_score = int(input("Team 1's final score: "))

number_of_stoppages = int(input("Enter number of stoppages: "))

if number_of_stoppages == 0:
    # Calculate DLS par score
    team2_target = team1_final_score + 1
    print("Team 2 Target: ",team2_target)
elif number_of_stoppages == 1: 
    """
    Case 1:
    Innings 1 is completed successfully, Innings 2 is reduced to x overs.
    where, x >20 [so, reduced by maximum of 30 overs]
    """
    
    """
    Take inputs for Team 2's innings:
    overs bowled
    runs scored
    wickets down
    overs lost/side
    """
    overs_bowled = int(input("Enter the number of overs bowled: "))
    runs_scored = int(input("Enter the number of runs scored: "))
    wickets_down = int(input("Enter the number of wickets down: "))
    overs_lost_per_side = int(input("Enter the number of overs lost per side: "))

    # In this case, Team 1 has used up all of its resources = 100% (for now)
    
    if overs_lost_per_side == 30:
        overs_left = 50 - overs_lost_per_side
        if wickets_down == 0:
            resources_left = 56.6

    revised_target = (team1_final_score * resources_left)/100

    print("Revised target for Team 2: ",revised_target)

else:
    pass

