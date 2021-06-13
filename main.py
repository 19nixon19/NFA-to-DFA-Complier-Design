import pandas as pd 
nfa = {}
n = int(input("Enter the total states in NFA: "))
t = int(input("Enter the number of transitions: "))
for i in range(n):
    state = input('State name: ')
    nfa[state] = {}
    for j in range(t):
        path = input("Enter the path: ")
        reaching_state = [x for x in input("Enter the end state from state {} travelling through path {}: ".format(state,path)).split()]
        nfa[state][path] = reaching_state
print("NFA")
print(nfa)
n_table = pd.DataFrame(nfa)
print(n_table.transpose())
n_final_state = [x for x in input("Enter the final states of NFA: ").split()]

#CONVERSION TO DFA
d_states = []
dfa = {}
key_list = list(list(nfa.keys())[0])
path_list = list(nfa[key_list[0]].keys())
dfa[key_list[0]] = {}
for y in range(t):
    var = "".join(nfa[key_list[0]][path_list[y]])
    dfa[key_list[0]][path_list[y]] = var
    if var not in key_list:
        d_states.append(var)
        key_list.append(var)
        
while len(d_states)!= 0:
    dfa[d_states[0]] = {}
    for _ in range(len(d_states[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(d_states[0])):
                temp += nfa[d_states[0][j]][path_list[i]]
            s = ""
            s = s.join(temp)
            if s not in key_list:
                d_states.append(s)
                key_list.append(s)
            dfa[d_states[0]][path_list[i]] = s
    d_states.remove(d_states[0])
print("DFA")
print(dfa)
d_table = pd.DataFrame(dfa)
print(d_table.transpose())

dfa_states = list(dfa.keys())
dfa_final = []
for x in dfa_states:
    for i in x:
        if i in n_final_state:
            dfa_final.append(x)
            break
print("Final states of DFA are: ",dfa_final)
