"""
Net run rate

The concept of net run rate involves subtracting the opponents' run rate from the team's run rate, i.e.
Match net run rate = (total runs scored / total overs faced) - (total runs conceded / total overs bowled)

For two teams which have just played, the winning side will have a positive Match NRR, and the losing side 
will have the negative of this (i.e. the Match NRRs will be additive inverses, summing to zero). 

~ Wikipedia
"""

def calculate_net_run_rate(total_runs_scored, total_balls_faced, total_runs_conceded, total_balls_bowled):
    print(total_runs_scored, total_balls_faced, total_runs_conceded, total_balls_bowled)
    team_run_rate = total_runs_scored / (total_balls_faced/6)
    opponent_run_rate = total_runs_conceded / (total_balls_bowled/6)
    net_run_rate = team_run_rate - opponent_run_rate
    return net_run_rate

print("First Team: ")
total_runs_scored_team1 = int(input("Enter the total runs scored: "))
total_overs_faced_team1 = float(input("Enter the total overs faced: "))
team1_whole_overs = int(total_overs_faced_team1)
team1_fractional_overs = round(total_overs_faced_team1 - team1_whole_overs, 1)
team1_balls_faced = team1_whole_overs * 6 + int(team1_fractional_overs * 10) * 1
# print(team1_balls_faced)

print("Second Team: ")
total_runs_scored_team2 = int(input("Enter the total runs scored: "))
total_overs_faced_team2 = float(input("Enter the total overs faced: "))
team2_whole_overs = int(total_overs_faced_team2)
team2_fractional_overs = round(total_overs_faced_team2 - team2_whole_overs, 1)
team2_balls_faced = team2_whole_overs * 6 + int(team2_fractional_overs * 10) * 1
# print(team2_balls_faced)

total_runs_conceded_team1 = total_runs_scored_team2
team1_balls_bowled = team2_balls_faced

total_runs_conceded_team2 = total_runs_scored_team1
team2_balls_bowled = team1_balls_faced

net_rr_team1 = calculate_net_run_rate(total_runs_scored_team1, team1_balls_faced, total_runs_conceded_team1, team1_balls_bowled)
net_rr_team2 = calculate_net_run_rate(total_runs_scored_team2, team2_balls_faced, total_runs_conceded_team2, team2_balls_bowled)

print(f"The first team's net run rate is: {net_rr_team1:.2f}")
print(f"The second team's net run rate is: {net_rr_team2:.2f}")

