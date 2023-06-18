def calculate_run_rate(total_runs, total_overs):
    run_rate = total_runs / total_overs
    return run_rate

# Scoring rate (runs/ball)
def calculate_scoring_rate(total_runs, total_balls):
    scoring_rate = total_runs / total_balls
    return scoring_rate

total_runs = 250
total_overs = 50
rr = calculate_run_rate(total_runs, total_overs)
print(f"The run rate is: {rr:.2f} runs per over")

total_balls = total_overs * 6
scoring_rate = calculate_scoring_rate(total_runs, total_balls)
print(f"The scoring rate is: {scoring_rate:.2f} runs per ball")
