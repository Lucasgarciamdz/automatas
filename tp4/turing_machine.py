import re

# class TuringMachine():
#     def __init__(self, states, alphabet, blank, initial_state, final_states, transitions):
#         self.states = states
#         self.alphabet = alphabet
#         self.blank = blank
#         self.initial_state = initial_state
#         self.final_states = final_states
#         self.transitions = transitions

#     def __str__(self):
#         return f"states: {self.states}\n" \
#                f"alphabet: {self.alphabet}\n" \
#                f"blank: {self.blank}\n" \
#                f"initial_state: {self.initial_state}\n" \
#                f"final_states: {self.final_states}\n" \
#                f"transitions: {self.transitions}\n"

#     def __repr__(self):
#         return f"TuringMachine({self.states}, {self.alphabet}, {self.blank}, {self.initial_state}, {self.final_states}, {self.transitions})"

def ejercicio_2a():
    pass


def ejercicio_2b():

    cadena = str(input("Ingrese la cadena que desea utilizar para la maquina de turing:"))
    states = {0, 1, 2, 4, 8}
    alphabet = {0, 1}
    blank = 0
    initial_state = 0
    final_states = {5}
    transitions = {
            (0, 0): (0, 0, 1),
            (0, 1): (0, 1, 2),
            (1, 0): (0, 0, 4),
            (1, 1): (0, 1, 8),
            (2, 0): (0, 0, 2),
            (2, 1): (0, 1, 4),
            (4, 0): (0, 0, 8),
            (4, 1): (0, 1, 0),
            (8, 0): (0, 0, 4),
            (8, 1): (0, 1, 2),
        }

    for x in cadena:
        