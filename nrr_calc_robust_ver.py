def calculate_net_run_rate(total_runs_scored, total_overs_faced, total_runs_conceded, total_overs_bowled):
    team_run_rate = total_runs_scored / total_overs_faced
    opponent_run_rate = total_runs_conceded / total_overs_bowled
    net_run_rate = team_run_rate - opponent_run_rate
    return net_run_rate

print("First Team: ")
total_runs_scored_team1 = int(input("Enter the total runs scored: "))
total_overs_faced_team1 = int(input("Enter the total overs faced: "))

print("Second Team: ")
total_runs_scored_team2 = int(input("Enter the total runs scored: "))
total_overs_faced_team2 = int(input("Enter the total overs faced: "))

total_runs_conceded_team1 = total_runs_scored_team2
total_overs_bowled_team1 = total_overs_faced_team2

total_runs_conceded_team2 = total_runs_scored_team1
total_overs_bowled_team2 = total_overs_faced_team1

net_rr_team1 = calculate_net_run_rate(total_runs_scored_team1, total_overs_faced_team1, total_runs_conceded_team1, total_overs_bowled_team1)
net_rr_team2 = calculate_net_run_rate(total_runs_scored_team2, total_overs_faced_team2, total_runs_conceded_team2, total_overs_bowled_team2)

print(f"The first team's net run rate is: {net_rr_team1:.2f}")
print(f"The second team's net run rate is: {net_rr_team2:.2f}")