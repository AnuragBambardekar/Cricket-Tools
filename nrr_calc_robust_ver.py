"""
Adding Features:

1. If a team is bowled out, the calculations don't use the number of overs actually bowled, but the full quota of overs to which the team was entitled (e.g. 50 overs for a One Day International, and 20 overs for a Twenty20 match)

2. If a match is interrupted, Duckworth-Lewis revised targets are set, and a result is subsequently achieved, the revised targets and revised overs are used for Team 1's innings (i.e. 1 run less than the final Target Score for Team 2, off the total number of overs allocated to Team 2), and the actual runs scored and overs used by Team 2 are used for Team 2's innings (as normal).
3. If a match is abandoned as a No Result, none of the runs scored or overs bowled count towards this calculation.
4. If a match is abandoned but a result decided by retrospectively applying Duckworth-Lewis, the number of overs assigned to each team for this calculation is the number of overs actually faced by Team 2. Team 1 is credited with Team 2's Par Score (the number of runs they would need to have reached from this number of overs and wickets lost if they were going to match Team 1's score), and the actual runs scored are used by Team 2 for Team 2's innings.
"""

"""
Scenarios:
1. Side that bats first wins

2. Side that bats second wins

3. Side that bats first is bowled out, side batting second wins
Team A bat first and are bowled out for 127 off 25.4 overs. Despite their run rate for the balls they faced being 127 / 25.667 = 4.95, because they were bowled out the entire 50 overs are added to their total overs faced tally for the tournament, and Team B are credited with having bowled 50 overs.
Team B reach the target off 30.5 overs, ending with 128–4. Team B actually scored at a slower pace (128/30.833 = 4.15), however they managed to protect their wickets and win. Thus, only the 30.833 overs are added to the seasonal tally.

4. Side that bats second is bowled out, side batting first therefore wins
Team A bat first and set a formidable 295–5 off their complement of 50 overs. Therefore, for the tournament NRR calculations, 295 runs and 50 overs are added to Team A's runs scored/overs faced tally and Team B's runs conceded/overs bowled tally.
Team B never get close, being bowled out for 116 off 35.4 overs. Therefore, as they were bowled out, 116 runs and 50 overs are added to Team A's runs conceded/overs bowled tally and Team B's runs scored/overs faced tally.

5. Both sides are bowled out, side batting first therefore wins

6. Game ends in a tie. [NRR=0]

7. Interrupted game with revised D/L target
In matches where Duckworth-Lewis revised targets are set due to interruptions which reduce the number of overs bowled, those revised targets and revised overs are used to calculate the NRR for both teams.
For example, Team A are dismissed for 165 in 33.5 overs. Team B progresses to 120–0, but play is halted after 18 overs due to rain.
Six overs are lost, and the target is reset to 150 from 44 overs, which Team B reach comfortably after 26.2 overs.

Because the target was revised to 150 runs from 44 overs, Team A's total is reset to 149 from 44 overs, thus their RR =
149/44 ≈ 3.39

Team B's RR, however, is computed as normal: 
150/26.33 ≈ 5.70

8. Abandoned game recorded as No Result [scores in such games are immaterial to NRR calculations.]

9. Abandoned game with retrospective D/L result
Team A score 254 runs from their 50 overs. Team B have scored 172–4 from 30 overs when the match is abandoned.
According to Duckworth-Lewis, 6 wickets and 20 overs in hand equates to 44.6% of resources, so Team B has used 55.4% of its resources, so their Par Score is 254 x 55.4% = 140.716 runs. As they are ahead of this, they are declared the winner.

~ [Wikipedia]
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

# team1_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
team1_whole_overs = int(total_overs_faced_team1)
team1_fractional_overs = round(total_overs_faced_team1 - team1_whole_overs, 1)
team1_balls_faced = team1_whole_overs * 6 + int(team1_fractional_overs * 10) * 1

print("Second Team: ")
total_runs_scored_team2 = int(input("Enter the total runs scored: "))
total_overs_faced_team2 = float(input("Enter the total overs faced: "))
total_wickets_lost_team2 = int(input("Enter the total wickets lost (0-10): "))

# team2_full_overs = 50  # Assuming 50 overs for One Day International (Modify as needed)
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
