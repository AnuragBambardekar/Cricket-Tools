"""
Adding Features:

1. If a team is bowled out, the calculations don't use the number of overs actually bowled, but the full quota of overs to which the team was entitled (e.g. 50 overs for a One Day International, and 20 overs for a Twenty20 match)

2. If a match is interrupted, Duckworth-Lewis revised targets are set, and a result is subsequently achieved, the revised targets and revised overs are used for Team 1's innings (i.e. 1 run less than the final Target Score for Team 2, off the total number of overs allocated to Team 2), and the actual runs scored and overs used by Team 2 are used for Team 2's innings (as normal).
3. If a match is abandoned as a No Result, none of the runs scored or overs bowled count towards this calculation.
4. If a match is abandoned but a result decided by retrospectively applying Duckworth-Lewis, the number of overs assigned to each team for this calculation is the number of overs actually faced by Team 2. Team 1 is credited with Team 2's Par Score (the number of runs they would need to have reached from this number of overs and wickets lost if they were going to match Team 1's score), and the actual runs scored are used by Team 2 for Team 2's innings.
"""


def calculate_net_run_rate(total_runs_scored, total_balls_faced, total_runs_conceded, total_balls_bowled):
    # print(total_runs_scored, total_balls_faced, total_runs_conceded, total_balls_bowled)
    team_run_rate = total_runs_scored / (total_balls_faced/6)
    # print(team_run_rate)
    opponent_run_rate = total_runs_conceded / (total_balls_bowled/6)
    # print(opponent_run_rate)
    net_run_rate = team_run_rate - opponent_run_rate
    return net_run_rate


print("First Team: ")
total_runs_scored_team1 = int(input("Enter the total runs scored: "))
total_overs_faced_team1 = float(input("Enter the total overs faced: "))
total_wickets_lost_team1 = int(input("Enter the total wickets lost (0-10): "))

team1_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
team1_whole_overs = int(total_overs_faced_team1)
team1_fractional_overs = round(total_overs_faced_team1 - team1_whole_overs, 1)
team1_balls_faced = team1_whole_overs * 6 + int(team1_fractional_overs * 10) * 1

print("Second Team: ")
total_runs_scored_team2 = int(input("Enter the total runs scored: "))
total_overs_faced_team2 = float(input("Enter the total overs faced: "))
total_wickets_lost_team2 = int(input("Enter the total wickets lost (0-10): "))

team2_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
team2_whole_overs = int(total_overs_faced_team2)
team2_fractional_overs = round(total_overs_faced_team2 - team2_whole_overs, 1)
team2_balls_faced = team2_whole_overs * 6 + int(team2_fractional_overs * 10) * 1

total_runs_conceded_team1 = total_runs_scored_team2
team1_balls_bowled = team2_balls_faced

total_runs_conceded_team2 = total_runs_scored_team1
team2_balls_bowled = team1_balls_faced

if total_wickets_lost_team1 == 10:
    team2_balls_bowled = 50 * 6
    team1_balls_faced = 50 * 6

if total_wickets_lost_team2 == 10:
    team1_balls_bowled = 50 * 6
    team2_balls_faced = 50 * 6

net_rr_team1 = calculate_net_run_rate(total_runs_scored_team1, team1_balls_faced, total_runs_conceded_team1, team1_balls_bowled)
net_rr_team2 = calculate_net_run_rate(total_runs_scored_team2, team2_balls_faced, total_runs_conceded_team2, team2_balls_bowled)


print(f"The first team's net run rate is: {net_rr_team1:.2f}")
print(f"The second team's net run rate is: {net_rr_team2:.2f}")
