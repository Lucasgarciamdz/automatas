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
#                f"transitions: {self.t ransitions}\n"

#     def __repr__(self):
#         return f"TuringMachine({self.states}, {self.alphabet}, {self.blank}, {self.initial_state}, {self.final_states}, {self.transitions})"




# def ejercicio_2a():
#     states = ["q0", "q1", "q2", "q3"]
#     transitions = ["x", "y"]
#     transitions_blank = ["x", "y", ""]
#     initial_state = ["q0"]
#     acceptance_state = ["q1", "q2", "q3"]
#     cadena = str(input("Ingrese la cadena que desea utilizar para la maquina de turing:"))
#     blank = 0
#     transitions = {
#         ("q0", "x"): ("q1", "x"),
#         ("q1", "x"): ("q2", "x"),
#         ("q1", "y"): ("q3", "y"),
#         ("q2", "x"): ("q2", "x"),
#         ("q2", "y"): ("q3", "y"),
#         ("q3", "x"): ("q2", "x"),
#         ("q3", "y"): ("q3", "y"),
#     }
#     transitions_blank = {
#         ("q0", ""):  ("q1", "x", "R"),
#         ("q1", ""):  ("q2", "y", "R"),
#         ("q2", ""):  ("q3", "x", "R"),
#     }
        
# def ejercicio_2b():

#     cadena = str(input("Ingrese la cadena que desea utilizar para la maquina de turing:"))
#     states = {0, 1, 2, 4, 8}
#     alphabet = {0, 1}
#     blank = 0
#     initial_state = 0
#     final_states = {5}
#     transitions = {
#             (0, 0): (0, 0, 1),
#             (0, 1): (0, 1, 2),
#             (1, 0): (0, 0, 4),
#             (1, 1): (0, 1, 8),
#             (2, 0): (0, 0, 2),
#             (2, 1): (0, 1, 4),
#             (4, 0): (0, 0, 8),
#             (4, 1): (0, 1, 0),
#             (8, 0): (0, 0, 4),
#             (8, 1): (0, 1, 2),
#         }

class Ejercicio_2a():

    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3"]
        self.transitions = ["x", "y"]
        self.transitions_blank = ["x", "y", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q1", "q2", "q3"]
        self.lambdas = {
            ("q0", "a"): ("q4", "a", "R"),
            ("q0", "b"): ("q1", "b", "R"),
            ("q1", "a"): ("q4", "a", "R"),
            ("q1", "b"): ("q2", "b", "R"),
            ("q2", "a"): ("q3", "a", "R"),
            ("q2", "b"): ("q2", "b", "R"),
            ("q3", "a"): ("q4", "a", "R"),
            ("q3", "b"): ("q2", "b", "R")
        }
        self.lambdas_states =[
            ["q1", "kboom"],
            ["q2", "q3"],
            ["q2", "q3"],
            ["q2", "q3"],
        ]

    def obtener_fil(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3}
        return rows.get(estado)

    def obtener_col(self, char):
        columns = {"x": 0, "y": 1}
        return columns.get(char)

    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fil(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True
        else:
            print("Rejected")
            return False

class Ejercicio_2b():

    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3"]
        self.transitions = ["a", "c"]
        self.transitions_blank = ["a", "c", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q2", "q3"]
        self.lambdas = {
            ("q0", "a"): ("q4", "a", "R"),
            ("q0", "b"): ("q1", "b", "R"),
            ("q1", "a"): ("q4", "a", "R"),
            ("q1", "b"): ("q2", "b", "R"),
            ("q2", "a"): ("q3", "a", "R"),
            ("q2", "b"): ("q2", "b", "R"),
            ("q3", "a"): ("q4", "a", "R"),
            ("q3", "b"): ("q2", "b", "R")
        }
        self.lambdas_states =[
            ["q1", "q2"],
            ["kboom", "q3"],
            ["q1", "q2"],
            ["q1", "q2"],
        ]

    def obtener_fil(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3}
        return rows.get(estado)

    def obtener_col(self, char):
        columns = {"a": 0, "c": 1}
        return columns.get(char)

    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fil(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True 
        else:
            print("Rejected")
            return False

class Ejercicio_2c():

    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3", "q4"]
        self.transitions = ["a", "b"]
        self.transitions_blank = ["a", "b", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q3", "q4"]
        self.lambdas = {
            ("q0", "a"): ("q4", "a", "R"),
            ("q0", "b"): ("q1", "b", "R"),
            ("q1", "a"): ("q4", "a", "R"),
            ("q1", "b"): ("q2", "b", "R"),
            ("q2", "a"): ("q3", "a", "R"),
            ("q2", "b"): ("q2", "b", "R"),
            ("q3", "a"): ("q4", "a", "R"),
            ("q3", "b"): ("q2", "b", "R")
        }
        self.lambdas_states =[
            ["q4", "q1"],
            ["q4", "q2"],
            ["q3", "q2"],
            ["q4", "q2"],
            ["q4", "q2"],
        ]

    def obtener_fil(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3, "q4": 4}
        return rows.get(estado)

    def obtener_col(self, char):
        columns = {"a": 0, "b": 1}
        return columns.get(char)

    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fil(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True
        else:
            print("Rejected")
            return False




if __name__ == "__main__":
    ejercicio_2c = Ejercicio_2c("bbaaa")
    ejercicio_2c.transactions()
    # ejercicio_2a = Ejercicio_2a("yx")
    # ejercicio_2a.transactions()
    # ejercicio_2b = Ejercicio_2b("aa")
    # ejercicio_2b.transactions()
    pass
