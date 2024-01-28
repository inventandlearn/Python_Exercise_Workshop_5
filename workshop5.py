import random 

def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop) 
    while tries != 0:
        
        print(f"Number of tries left: {tries}")
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == random_number:
            print("You guessed the correct number!")
            exit()
        elif guess < random_number:
            print("Guess higher!")
        elif guess > random_number:
            print("Guess lower!")
        tries -= 1
    print(f"You have run out of attempts! The correct guess is {random_number}")


# ---- Test Driver Code 1 -----
# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    
    random_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {random_number}")   
    for program_guess in range(stop + 1):
        print((f"Number of tries left: {tries}"))
        print((f"The program is guessing..... {program_guess}")) 
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return
        if program_guess == random_number:
                print("The program has guessed the correct number!")
                exit()
        tries -= 1            
    

# ---- Test Driver Code 2 -----    
# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    
    random_number = random.randint(start, stop)
    print(f"The random number to find is: {random_number}")
    lower_bound = start
    upper_bound = stop
    while tries != 0 and lower_bound <= upper_bound:
        
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot
        if pivot_value == random_number:
            print(f"Found it! {random_number}")
            return pivot
        if pivot_value > random_number:
            upper_bound = pivot - 1
            print("Guessing lower!")
        elif pivot_value < random_number: 
            lower_bound = pivot + 1
            print("Guessing higher!")
        tries -= 1
    print("Your program has failed to find the number!")
    return -1

# ---- Test Driver Code 3 -----      
# guess_random_num_binary(5, 0, 100) 