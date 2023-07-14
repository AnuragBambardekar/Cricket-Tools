def calculate_tournament_net_run_rate(total_runs_scored, balls_faced, total_runs_conceded, balls_bowled):
    
    # print(balls_bowled, balls_faced, total_runs_scored, total_runs_conceded)
    
    tournament_run_rate = total_runs_scored / (balls_faced/6)
    # print(tournament_run_rate)
    tournament_opponent_run_rate = total_runs_conceded / (balls_bowled/6)
    # print(tournament_opponent_run_rate)
    tournament_net_run_rate = tournament_run_rate - tournament_opponent_run_rate
    return tournament_net_run_rate

num_matches = int(input("Enter the number of matches: "))

total_runs_scored = 0
total_overs_faced = 0
total_runs_conceded = 0
total_overs_bowled = 0

for i in range(num_matches):
    print(f"Match {i+1}:")
    runs_scored = int(input("Enter the total runs scored: "))
    overs_faced = float(input("Enter the total overs faced: "))
    wickets_lost = int(input("Enter the total wickets lost (0-10): "))
    runs_conceded = int(input("Enter the total runs conceded: "))
    overs_bowled = float(input("Enter the total overs bowled: "))
    wickets_taken = int(input("Enter the total wickets taken (0-10): "))

    if wickets_lost == 10:
        overs_faced = 50

    if wickets_taken == 10:
        overs_bowled = 50

    total_runs_scored += runs_scored
    total_overs_faced += overs_faced
    total_runs_conceded += runs_conceded
    total_overs_bowled += overs_bowled



whole_overs_faced = int(total_overs_faced)
fractional_overs = round(total_overs_faced - whole_overs_faced, 1)
balls_faced = whole_overs_faced * 6 + int(fractional_overs * 10) * 1

whole_overs_bowled = int(total_overs_bowled)
fractional_overs = round(total_overs_bowled - whole_overs_bowled, 1)
balls_bowled = whole_overs_bowled * 6 + int(fractional_overs * 10) * 1

# print(total_runs_scored)
# print(total_runs_conceded)
# print(balls_faced)
# print(balls_bowled)



tournament_net_rr = calculate_tournament_net_run_rate(total_runs_scored, balls_faced, total_runs_conceded, balls_bowled)
print(f"The tournament net run rate is: {tournament_net_rr:.3f}")