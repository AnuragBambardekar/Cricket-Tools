# Cricket Tools

- Simple Run Rate calculator
- Net Run Rate calculator - (doesn't support bowled out scenarios)
- Tournament Run Rate calculator
- Overs to Balls Calculator
- NRR Calculator - v2
- Tournament Run Rate Calculator - v2

- Feature added:
    - If a team is bowled out, the calculations don't use the number of overs actually bowled, but the full quota of overs to which the team was entitled (e.g. 50 overs for a One Day International, and 20 overs for a Twenty20 match)

# Criticisms 

NRR does not accurately reflect margins of victory, as it takes no account of wickets lost. <br>
NRR takes into account only - overs faced/bowled; *Duckworth-Lewis-Stern* states that teams have two resources - overs and wickets. <br>
A narrow victory can produce a higher NRR than a comfortable victory. <br>

New Zealand narrowly beat Sri Lanka by bowling them out for 138, then reaching 139–9 from 36.3 overs, giving them match NRR = (139/36.5) − (138/50) = 1.05.

Sri Lanka comfortably beat England by restricting them to 293–7 from 50 overs, then reaching 297–3 from 47.1 overs, giving them match NRR = (297/47.167) − (293/50) = 0.44.

This fact can encourage a team to play in an overly aggressive manner, to maximise NRR by batting with next to no regard for preserving wickets, when the required run rate alone seems low, which can then put the team in danger of losing.

- NRR may be manipulated [~ 1999 World Cup Group B - Aus vs WI]


# Alternatives to NRR

- Duckworth-Lewis-Stern Method

## TO Do:

- DLS Calculator


## Refs
- Wikipedia: https://en.wikipedia.org/wiki/Net_run_rate