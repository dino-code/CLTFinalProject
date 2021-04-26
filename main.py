def print_output(step, curr_state, unread_input, stack, delta_rule, r_rule):
    # This method prints the output of each row (step) in the output table.
    print('step:', step)
    print('curr_state:', curr_state)
    print('unread_input:', unread_input)
    print('stack', *stack) # prints stack in one line
    print('delta_rule', delta_rule)
    print('r_rule', r_rule)

inputs = [
    "ab$", "aabb$", "aaabbb$", "aaaabbbb$", 
    "aaaaabbbbb$", "aaaaaabbbbbb$",
    "aaaaaaabbbbbbb$", "aaaaaaaabbbbbbbb$", 
    "aaaaaaaaabbbbbbbbb$", "aaaaaaaaaabbbbbbbbbb$"
]

delta_rules = {
    ('p', 'e', 'e') : 1, ('q', 'a', 'e') : 2,
    ('q_a', 'e', 'a') : 3, ('q', 'b', 'e') : 4,
    ('q_b', 'e', 'b') : 5, ('q', '$', 'e') : 6,
    ('q_a', 'e', 'S') : 6, ('q_a', 'e', 'S') : 7,
    ('q_b', 'e', 'S') : 8
}

for unread_input in inputs:
    # initial start state for each unread_input
    curr_state = 'p'
    stack = []
    step = 0
    delta_rule = 'null'
    r_rule = 'null'


    print(step + curr_state + unread_input Stack delta rule R rule) # headers
    print(step + 'p' + input + stack + dela_rule, r_rule) #printing first step

    curr_state = 'q'
    stack.append('S')

    while (curr_state != 'q_$'):
        top_of_stack = stack[-1]
        top_of_unread_input=unread_input[0]
        step+=1
        if curr_state=='q': #(this is a lookahead state)
            next_state = delta_rules[(curr_state, top_of_unread_input[0])]      #should return q_a or q_b
            
            if next_state == 'q_$':
                if stack.empty():
                    curr_state = 'q_$'
                    #delta_rule
                    return True	
                else:
                    return False
            temp_delta_rule=delta_rules[(curr_state,top_of_unread_input,'e')]
            unread_input=unread_input[:-1]
            curr_state = next_state


        if curr_state == 'q_a' or curr_state == 'q_b':
            next_state = dict[(curr_state, top_of_unread_input[0])] 
            temp_delta_rule=delta_rules[(curr_state,'e',top_of_stack)]
            if top_of_stack == curr_state[-1]:    # will be a or b
                curr_state = 'q'
                stack.pop()
            if top_of_stack == 'S':
                stack.pop()
                if curr_state == 'q_a':
                    stack.append('b')
                    stack.append('S')
                    stack.append('a')
            curr_state = next_state
            
            

        
        print_output(step, curr_state, unread_input, stack, temp_delta_rule, r_rule)