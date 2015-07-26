actual = map(int, raw_input().split()) # stores actual return date (D M Y)
expected = map(int, raw_input().split()) # stores expected return date (D M Y)

yearFine = 10000 # initialize the year fine
monthFine = 500 # intialize the monthly fine
dayFine = 15 # intialize the daily fine
noFine = 0 # value for no fine

if actual[2] != expected[2]: # case where the return is in a different year
    
    if actual[2] < expected[2]: # case where the return is early
        print noFine # total fine
    
    else: # case where the return is late
        print yearFine # total fine (for years fine is fixed)
    
elif actual[1] != expected[1]: # case where the return is same year but different month
    
    if actual[1] < expected[1]: # case where the return is early
        print noFine # total fine
    
    else: # case where the return is late
        monthDiff = actual[1] - expected[1] # how many months late the return is
        print monthFine * monthDiff # total fine
    
elif actual[0] > expected[0]: # case where the return is same year,same month, but different day
    dayDiff = actual[0] - expected[0] # how many days late the return is
    print dayFine * dayDiff # total fine
    
else: # all other cases
    print noFine
