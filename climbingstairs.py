def climbingStairs(n):
    if n <= 2:
        return n
    
    two_steps_back = 1
    one_step_back = 2
    for i in range(3, n +1):
        current = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = current
    
    return one_step_back