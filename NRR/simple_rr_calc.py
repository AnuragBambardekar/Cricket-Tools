"""
Run rate calculator

run rate = total runs scored / total overs faced

~ Wikipedia
"""

def calculate_run_rate(total_runs, total_balls):
    run_rate = total_runs / total_balls
    # per over run rate
    run_rate *= 6
    return run_rate

# Scoring rate (runs/ball)
def calculate_scoring_rate(total_runs, total_balls):
    scoring_rate = total_runs / total_balls
    return scoring_rate

total_runs = int(input("Enter the total runs: "))
total_overs = float(input("Enter the total overs: "))

whole_overs = int(total_overs)
fractional_overs = round(total_overs - whole_overs, 1)

balls = whole_overs * 6 + int(fractional_overs * 10) * 1

rr = calculate_run_rate(total_runs, balls)
print(f"The run rate is: {rr:.2f} runs per over")

scoring_rate = calculate_scoring_rate(total_runs, balls)
print(f"The scoring rate is: {scoring_rate:.2f} runs per ball")
