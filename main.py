inputs = ['aabb']

For input in inputs:
Curr_state = 'p'
Stack = []
    # for actual program have a vector of inputs.
	step = 0
	Delta_rule = 'null'
	R_rule = 'null'

	print(Step State unread_input Stack delta rule R rule) # headers
	print(step + 'p' + input + stack +dela_rule, r_rule) #printing first step

	Curr_state = 'q'
	stack.push(S)

While (curr_state != ‘q_$’)

step+=1
If curr_state==q: (this is a lookahead state)
    Next_state = dict[(curr_state, unread_input[0])]      #should return q_a or q_b
    If next_state == q_$:
        If stack.empty():
            Curr_state = q_$
            delta_rule
        
            Return True	
        Else:
	  Return False
			Curr_state = next_state

If curr_state == 'q_a' or curr_state == 'q_b':
	Top_of_stack = stack.at.top
	If top_of_stack == curr_state[-1]:    # will be a or b
		curr_state = q
		stack.pop()
	If top_of stack == 'S':
		stack.pop()
		If curr_state == q_a:
			push(b)
			push(S)
			push(a)
	


Print (step,curr_state, read_input, top_of_stack)