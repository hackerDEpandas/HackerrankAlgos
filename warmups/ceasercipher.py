N = input() # length of string
S = raw_input() # the string to be encrypted
K = input() # stores the key integer

if K > 26: # case where the key value is larger than 26
    K = K % 26 # change K to K mod 26 (ex: if K = 56, then 56 mod 26 = 4, and K would equal 4)

finalStr = '' # initialize finalStr, to be appended later

for symbol in S: # begin iterating through each symbol in the string
    translation = '' # a place to store the symbol after a letter has been translated

    if symbol.isalpha(): # case where symbol is a letter in the alphabet
        num = ord(symbol) # gives the ordinal number for symbol
        num += K # add the ordinal number to the key integer
        
        if symbol.isupper(): # case where symbol is an uppercase letter
            
            if num > ord('Z'): # case where num is bigger than 90 [90 = ord('Z')]
                num -= 26 # assign num to the proper ordinal number

        elif symbol.islower(): # case where symbol is a lowercase letter
            
            if num > ord('z'): # case where num is bigger than 122 [122 = ord('z')]
                num -= 26 # assign num to the proper ordinal number
        
        translation += chr(num) # updates translation with the new encrypted letter        
    else: # case where symbol is any character besides a letter in the alphabet
        translation += symbol # updates translation with symbol
    
    finalStr += translation # append translation to finalStr after each iteration  
print finalStr # print the finished encrypted message
