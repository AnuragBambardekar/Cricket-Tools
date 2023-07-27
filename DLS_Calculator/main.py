print("Duckworth-Lewis-Stern Calculator for ODI regulations(50 overs/innings) (min. 20 overs/side)")

"""
overs/innings must be less than 100 and must be a whole number
"""
while True:
    try:
        initial_overs = int(input("Overs at the start of the match [not more than 50 overs]: "))
        if 1 <= initial_overs < 100:
            break
        else:
            print("Invalid input. Please enter a value between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Valid input:", initial_overs)


team1_final_score = int(input("Team 1's final score: "))

number_of_stoppages = int(input("Enter number of stoppages: "))

if number_of_stoppages == 0:
    # Calculate DLS par score
    pass
else:
    # Take inputs for each stoppage:
    """
    overs bowled
    runs scored
    wickets down
    overs lost/side
    """
    pass

