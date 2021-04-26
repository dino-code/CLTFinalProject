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
    # delta_rules[(curr_state, next_input, top_of_stack)]
    # example delta_rules[('p', 'e', 'e')] = ('1. (p, e, e) -> (q, S)', 'q')
    ('p', 'e', 'e') : ('1. (p, e, e) -> (q, S)', 'q'), 
    ('q', 'a', 'e') : ('2. (q, a, e) -> (q_a, e)', 'q_a'),
    ('q_a', 'e', 'a') : ('3. (q_a, e, a) -> (q, e)', 'q'), 
    ('q', 'b', 'e') : ('4. (q, b, e) -> (q_b, e)', 'q_b'),
    ('q_b', 'e', 'b') : ('5. (q_b, e, b) -> (q, e)', 'q'), 
    ('q', '$', 'e') : ('6. (q, $, e) -> (q_$, e)', 'q_$'),
    ('q_a', 'e', 'S') : ('7. (q_a, e, S) -> (q_a, aSb)', 'q_a'),
    ('q_b', 'e', 'S') : ('8. (q_b, e, S) -> (q_b, e)', 'q_b')
}

r_rules = {
    # r_rule key is the value of delta_rule
    # example r_rules[delta_rules[('q_a', 'e', 'S')]] = 'S -> aSb'
    ('7. (q_a, e, S) -> (q_a, aSb)', 'q_a') : 'S -> aSb', 
    ('8. (q_b, e, S) -> (q_b, e)', 'q_b') : 'S -> e'
}

for unread_input in inputs:
    # initial start state for each unread_input
    curr_state = 'p'
    stack = []
    step = 0
    delta_rule = 'null'
    r_rule = 'null'

    # print step 0
    print_output(step, curr_state, unread_input, stack, delta_rule, r_rule)

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
            unread_input.pop()
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
            
            


        print (step, ' ', curr_state, ' ', unread_input, ' ', top_of_stack, ' ', temp_delta_rule)