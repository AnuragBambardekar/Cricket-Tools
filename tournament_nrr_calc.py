"""
Tournament Net run rate

A team's overall NRR for a tournament is not defined as the sum or average of the NRR's from the individual matches, but as:
Tournament Net Run Rate = (Total runs scored in all matches / Total overs faced in all matches) - (Total runs conceded in all matches / Total overs bowled in all matches)
"""

def calculate_tournament_net_run_rate(total_runs_scored, balls_faced, total_runs_conceded, balls_bowled):
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
    runs_conceded = int(input("Enter the total runs conceded: "))
    overs_bowled = float(input("Enter the total overs bowled: "))

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
print(f"The tournament net run rate is: {tournament_net_rr:.2f}")

"""
FOR
South Africa had scored, so far in the tournament:

Against India, 254 runs (for 6 wkts) from 47.2 overs
Against Sri Lanka, 199 runs (for 9 wkts) from 50 overs
Against England, 225 runs (for 7 wkts) from 50 overs
Across the three games, South Africa scored 678 runs in a total of 147 overs and 2 balls (actually 147.333 overs), a rate of 678/147.333 or 4.602 rpo.

AGAINST
Teams opposing South Africa scored:
India, 253 (for 5 wkts) from 50 overs.
Sri Lanka, 110 all out from 35.2 overs.
England, 103 all out from 41 overs.
In the case of Sri Lanka and England, because they were all out before their allotted 50 overs expired, the run rate is calculated as if they had scored their runs over the full 50 overs.

Therefore, the run-rate scored against South Africa across the first three games is calculated on the basis of 466 runs in a total of 50 + 50 + 50 = 150 overs, a rate of 466/150 or 3.107 rpo.

NET-RR
The net run-rate is, therefore,

  4.602  Run-rate for 
  3.107  Run-rate against 
  ===== 
+ 1.495  ANSWER 
  ===== 

  ~ ESPN cricinfo

"""