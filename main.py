inputs = ['aabb']

delta_rules = {
    ('p', 'e', 'e') : 1, ('q', 'a', 'e') : 2,
    ('q_a', 'e', 'a') : 3, ('q', 'b', 'e') : 4,
    ('q_b', 'e', 'b') : 5, ('q', '$', 'e') : 6,
    ('q_a', 'e', 'S') : 6



}

for input in inputs:
    curr_state = 'p'
    stack = []
    # for actual program have a vector of inputs.
	step = 0
	delta_rule = 'null'
	r_rule = 'null'

	print(step State unread_input Stack delta rule R rule) # headers
	print(step + 'p' + input + stack +dela_rule, r_rule) #printing first step

	Curr_state = 'q'
	stack.push(S)

while (curr_state != ‘q_$’):

    step+=1
    if curr_state=='q': #(this is a lookahead state)
        next_state = dict[(curr_state, unread_input[0])]      #should return q_a or q_b
        if next_state == 'q_$':
            if stack.empty():
                curr_state = 'q_$'
                delta_rule
                return True	
            else:
                return False
    
    curr_state = next_state

    if curr_state == 'q_a' or curr_state == 'q_b':
        top_of_stack = stack[-1]
        if top_of_stack == curr_state[-1]:    # will be a or b
            curr_state = 'q'
            stack.pop()
        if top_of stack == 'S':
            stack.pop()
            If curr_state == 'q_a':
            
                stack.append('b')
                stack.append('S')
                stack.append('a')
        


    print (step,curr_state, unread_input, top_of_stack)