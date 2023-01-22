#Assignment 7 by Blake Gerold

# This CSP class is the basis for a generic Contraint Satisfaction Problem class
# Its intended use is to use as a base class to be overridden
# the function for consistent or chooseVariable can be overridden in a subclass

import copy

class CSP:

    def __init__ (self, variables, domains):
        # a list of variables
        # a dictionary of domains: a mapping of variables to a list of possible values
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for v in variables:
            self.constraints[v] = []


    def addConstraint(self, variable1, variable2):
        # add a contaraint that variable 1 and variable 2 do not have the same value
        if variable2 not in self.constraints[variable1]:
            self.constraints[variable1].append(variable2)
        if variable1 not in self.constraints[variable2]:
            self.constraints[variable2].append(variable1)

    def ac3(self):
        # Arc-Consistancy 3
        # limits the domains of variables in the CSP that can't be satisfied
        arcs = []
        for variable1 in self.variables:
            for variable2 in self.constraints[variable1]:
                arcs.append((variable1, variable2))

        while len(arcs) > 0:
            arc = arcs.pop(0)
            variable1 = arc[0]
            if self.revise(variable1, arc[1]):
                if len(self.domains[variable1]) == 0:
                    return False

                for variable2 in self.constraints[variable1]:
                    if (variable2 != arc[1]):
                        arcs.append((variable2, variable1))
        return True


    def revise(self, variable1, variable2):
        # for each the values in the domain of variable 1
        # checks if there exists a value in variable2's domain the doesn't conflict
        # if no such value exists, remove the value from the domain of variable 1
        revised = False

        for val in self.domains[variable1]:
            satisfied = False

            for val2 in self.domains[variable2]:
                if val != val2:
                    satisfied = True

            if not satisfied:
                self.domains[variable1].remove(val)
                revised = True

        return revised


    def search(self):
        # use backtracking search to find a solution
        # updates the domains of each of the variables

        assignment = {}
        for variable in self.variables:
            if len(self.domains[variable]) == 1:
                assignment[variable] = self.domains[variable][0]

        solution = self.backtrack(assignment)

        if solution is not None:
            for variable in self.variables:
                self.domains[variable] = [solution[variable]]

    def solved(self):
        # return True if each variable has domain of lenth 1
        # and contraints are all not violated
        for variable in self.variables:
            if len(self.domains[variable]) != 1:
                return False
        return self.validateSolution()

    def validateSolution(self):
        # tests the contraints
        # if the value in the domain of a variable matchs the
        # value in a variable that is restricted by a constraint, return False
        # Otherwise; return True
        for variable1 in self.variables:
            for variable2 in self.constraints[variable1]:
                if self.domains[variable1][0] == self.domains[variable2][0]:
                    return False
        return True



    def consistent(self, variable, val, assignment):
        # inputs: a variable, a proposed value, and an assignment dictionary
        # returns False if assigning the val to the variable would conflict
        # with a constraint as another variable in the assignment is already assigned the val
        # otherwise, return True
        for variable2 in self.constraints[variable]:
            if variable2 in assignment and assignment[variable2] == val:
                return False
        return True

    def impossible(self):
        # returns True if the domain of any variable is empty -- no possible values
        # otherwise False
        for variable in self.variables:
            if len(self.domains[variable]) == 0:
                return True
        return False

    def backtrack(self, assignment):
        # input an assignment -- a dictionary between variables and a value
        # recursively search for a possible assignment that satisfies all contraints
        # returns an assignment mapping
        #TODO: Implement backtrack function here based on pseudocode on last slide from Day 21
        #use copy.deepcopy() for the copying steps
        #var = 0
        #new_assignment = {}
        #new_csp = copy.deepcopy(self)
        #result = {}

        #check of complete assignment by checking assignment length vs. number of variables
        if len(assignment) == len(self.variables):
            return assignment
        
        #use predefined chooseVariable(), consistent(), impossible() functions in this step
        var = self.chooseVariable(assignment)
         
        for value in self.domains[var]:
            if self.consistent(var, value, assignment):
                new_assignment = copy.deepcopy(assignment)
                new_assignment[var] = value
                new_csp = copy.deepcopy(self)
                new_csp.domains[var] = [value]
                new_csp.ac3()
                
                for v in new_csp.variables:
                    if len(self.domains) == 1:
                        new_assignment[v] = new_csp.domains[v][0] 
                if not new_csp.impossible():
                    result = new_csp.backtrack(new_assignment)
                    if result:
                        return result

    def chooseVariable(self, assignment):
        # return a variable that is not in the assignment
        for v in self.variables:
            if v not in assignment:
                return v
        return None


    def print(self):
        # print out each variable and its domain values
        result = ""
        for variable in self.variables:
            result += str(variable) + " : " + str(self.domains[variable]) + "\n"
        print(result)
