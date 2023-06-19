def overs_to_balls(overs):
    # print(type(overs))
    whole_overs = int(overs)
    # print(whole_overs)
    # print(overs)
    fractional_overs = round(overs - whole_overs, 1)
    # print(fractional_overs)
    balls = whole_overs * 6 + int(fractional_overs * 10) * 1
    return balls

# Example usage
overs = 40.3
balls = overs_to_balls(overs)
print(f"{overs} overs is equal to {balls} balls.")
