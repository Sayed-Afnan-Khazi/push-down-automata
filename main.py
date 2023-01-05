# A Push Down Automata to accept input strings of the form 0^n 1^4n


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
    # State: {Read: {Stack: (Next State, Stack Action)}}
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
def PDA(input_string,print_output = True):
    global stk
    '''
    This function takes an input string and runs the Push Down Automata on it.
    This PDA accept input strings of the form 0^n 1^4n
    '''
    input_string = input_string+'e' # Adding an epsilon to the end of the string
    
    current_state = 'q0'
    running_string = ''
    
    for i in input_string:
        
        # Look up the transition to be done
        transition = transitions[current_state][i][stk[-1]] # Get the transition
        current_state = transition[0] # Get the next state

        if print_output:
            running_string += i
            print("*"*80)
            print("Running String:",running_string)
            print("String Read:",i)
            print("Current State:",current_state)
            print("Stack:",stk)

        # Check if the automata has reached a final state
        if current_state == 'reject':
            print("Rejected")
            return 1
            break
        elif current_state == 'q2':
            print("Accepted")
            return 0
            break

        # Or else, execute the transition
        exe = transition[1] # Get the stack action to be executed
        stk = stk[:-1] # Pop the topmost element of the stack
        exe() # Execute the stack action (push into the stack)

if __name__ == '__main__':
    # Take an example input string
    input_string = '01111'
    PDA(input_string)
