"""
Adding Features:

1. If a team is bowled out, the calculations don't use the number of overs actually bowled, but the full quota of overs to which the team was entitled (e.g. 50 overs for a One Day International, and 20 overs for a Twenty20 match)
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
total_wickets_lost_team1 = int(input("Enter the total wickets lost (0-10): "))

team1_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
team1_whole_overs = float(total_overs_faced_team1)
team1_fractional_overs = round(total_overs_faced_team1 - team1_whole_overs, 1)
team1_balls_faced = team1_full_overs * 6 if total_overs_faced_team1 == team1_full_overs else team1_whole_overs * 6 + int(team1_fractional_overs * 10) * 1

print("Second Team: ")
total_runs_scored_team2 = int(input("Enter the total runs scored: "))
total_overs_faced_team2 = float(input("Enter the total overs faced: "))
total_wickets_lost_team2 = int(input("Enter the total wickets lost (0-10): "))

team2_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
team2_whole_overs = float(total_overs_faced_team2)
team2_fractional_overs = round(total_overs_faced_team2 - team2_whole_overs, 1)
team2_balls_faced = team2_full_overs * 6 if total_overs_faced_team2 == team2_full_overs else team2_whole_overs * 6 + int(team2_fractional_overs * 10) * 1

total_runs_conceded_team1 = total_runs_scored_team2
total_overs_bowled_team1 = total_overs_faced_team2
team1_whole_overs = float(total_overs_bowled_team1)
team1_fractional_overs = round(total_overs_bowled_team1 - team1_whole_overs, 1)
team1_balls_bowled = team1_whole_overs * 6 + int(team1_fractional_overs * 10) * 1

total_runs_conceded_team2 = total_runs_scored_team1
total_overs_bowled_team2 = total_overs_faced_team1
team2_whole_overs = float(total_overs_bowled_team2)
team2_fractional_overs = round(total_overs_bowled_team2 - team2_whole_overs, 1)
team2_balls_bowled = team2_whole_overs * 6 + int(team2_fractional_overs * 10) * 1

if total_wickets_lost_team1 == 10 or total_wickets_lost_team2 == 10:
    team1_balls_bowled = team1_balls_faced = team1_full_overs * 6
    team2_balls_bowled = team2_balls_faced = team2_full_overs * 6

net_rr_team1 = calculate_net_run_rate(total_runs_scored_team1, team1_balls_faced, total_runs_conceded_team1, team1_balls_bowled)
net_rr_team2 = calculate_net_run_rate(total_runs_scored_team2, team2_balls_faced, total_runs_conceded_team2, team2_balls_bowled)


print(f"The first team's net run rate is: {net_rr_team1:.2f}")
print(f"The second team's net run rate is: {net_rr_team2:.2f}")
