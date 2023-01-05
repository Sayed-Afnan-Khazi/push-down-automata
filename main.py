# A Push Down Automata to accept input strings of the form 0^n 1^4n

# Take an input string

input_string = '011111111e'

# Create a stack/list

stk = 'z'

# Make the state rules (the transition table)

def pushFour():
    global stk
    stk = stk+'00000'

def nothing():
    pass

def pushFourWithZ():
    global stk
    stk = stk+'z0000'

transitions = {
    'q0': {
        '0': {'z': ('q0',pushFourWithZ), '0': ('q0',pushFour),'1': ('reject',nothing),'e':('reject',nothing)},
        '1': {'z': ('reject',nothing), '0': ('q1',nothing),'1': ('reject',nothing),'e':('reject',nothing)},
        'e': {'z': ('reject',nothing), '0': ('reject',nothing),'1': ('reject',nothing),'e':('q1',nothing)},
    },
    'q1': {
        '0': {'z': ('reject',nothing), '0': ('reject',nothing),'1': ('reject',nothing),'e':('reject',nothing)},
        '1': {'z': ('reject',nothing), '0': ('q1',nothing),'1': ('reject',nothing),'e':('reject',nothing)},
        'e': {'z': ('q2',nothing), '0': ('reject',nothing),'1': ('reject',nothing),'e':('q1',nothing)},
    },
    'q2': {},
}


# Start the automata
current_state = 'q0'
running_string = ''
for i in input_string:
    # Look up the transition to be done
    transition = transitions[current_state][i][stk[-1]] # Get the transition
    current_state = transition[0] # Get the next state
    running_string += i
    print("*"*80)
    print("Running String:",running_string,)
    print("String Read:",i)
    print("Current State:",current_state)
    print("Stack:",stk)
    if current_state == 'reject':
        print("Rejected")
        break
    elif current_state == 'q2':
        print("Accepted")
        break
    exe = transition[1] # Get the stack action to be executed
    stk = stk[:-1]
    exe() # Execute the stack action
