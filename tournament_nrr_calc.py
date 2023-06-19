"""
Tournament Net run rate

A team's overall NRR for a tournament is not defined as the sum or average of the NRR's from the individual matches, but as:
Tournament Net Run Rate = (Total runs scored in all matches / Total overs faced in all matches) - (Total runs conceded in all matches / Total overs bowled in all matches)
"""

def calculate_tournament_net_run_rate(total_runs_scored, total_overs_faced, total_runs_conceded, total_overs_bowled):
    tournament_run_rate = total_runs_scored / total_overs_faced
    tournament_opponent_run_rate = total_runs_conceded / total_overs_bowled
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
    overs_faced = int(input("Enter the total overs faced: "))
    runs_conceded = int(input("Enter the total runs conceded: "))
    overs_bowled = int(input("Enter the total overs bowled: "))

    total_runs_scored += runs_scored
    total_overs_faced += overs_faced
    total_runs_conceded += runs_conceded
    total_overs_bowled += overs_bowled

tournament_net_rr = calculate_tournament_net_run_rate(total_runs_scored, total_overs_faced, total_runs_conceded, total_overs_bowled)
print(f"The tournament net run rate is: {tournament_net_rr:.2f}")
