import csv
import sys

# list of input files
input_files = ['adjacency_matrix_US.csv']
# available colors
colors = ['Red', 'Green', 'Blue', 'Yellow', 'no color']


# class which drives program, takes state matrix as input variable, and contains color
# assignment algorithm. Sends final_colors matrix to output which then prints color
# layout to console and to output file
class ColorStates:
    def __init__(self, states, output_file):
        self.size = len(states) - 1         # amount of states
        self.map = graph(states)            # graph (map) of each state's adjacency (2D array)
        self.totalnva = 0                   # total assignments
        self.nva = 0                        # number of variable assignments
        self.color_size = len(colors) - 1   # number of colors

        # checks if colors are safe
        # s -> current state | color -> current color
        def check(self, s, color, state_colors):
            for i in range(self.size):
                # if state has adjacency
                if self.map[s][i] == '1':
                    # if colors match
                    if state_colors[i] == color:
                        # color failure
                        return False
            # all pass then return true
            return True

        # recursive backtracking function
        def colormap(self, s, state_colors, color_size):
            # print(state_colors)           # prints every step in algorithm
            if s == self.size:              # last element reached
                return True                 # stop recursion by true return
            # assign color to state (starting at red), try every color until true
            for color in range(0, color_size):
                # ensure color safe to assign
                if check(self, s, color, state_colors):
                    state_colors[s] = color # assign color
                    self.nva += 1           # increment variable assignment
                    self.totalnva += 1      # increment total assignments
                    # color safe, so try with next state
                    if colormap(self, s + 1, state_colors, color_size):
                        return True         # return control to previous call
                    state_colors[s] = 4     # color failed, assign 'no color'
                self.totalnva += 1  # increment variable assign

        # create color list with 'no color' as default
        state_colors = [4] * self.size
        colormap(self, 0, state_colors, self.color_size)    # algorithm start
        final_colors = state_colors         # final state colors
        output_colors(states, final_colors, self.nva, self.totalnva, output_file)


# outputs final color layout to console and output file
def output_colors(states, state_colors, nva, totalnva, output_file):
    sys.stdout = open(output_file, 'w')
    print("Number of variable assignments (nva) (including reassignments): ", nva)
    print("Total attempted assignments (including failures): ", totalnva)
    print("-----------------------------------------------------------------------------------------------------------")
    print("State\t\t\t| Adjacent Variables")
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(1, len(states)):
        print('{:20}{:<5}'.format(''.join(states[i][0][0]), "-> {"), end='')
        has_adjacent = 0
        for j in range(1, len(states)):
            if states[i][0][j] == '1':
                print(states[0][0][j] + ':' + colors[state_colors[j - 1]] + ', ', end='')
                has_adjacent = 1
        if has_adjacent == 0:
            print("No adjacent variables ", end='')

        print("}")

    print("\n")
    print("----------------------------------------")
    print("State\t\t\t| Color\t")
    print("----------------------------------------")
    for i in range(1, len(states)):
        print('{:20}{:<5}'.format(''.join(states[i][0][0]), colors[state_colors[i - 1]]))
    print("\n\n")


# returns an adjacency graph (omitting state name)
# essentially removes state names from graph
def graph(states):
    graph = []
    for i in range(1, len(states)):
        graph.append(states[i][0][1::])
    return graph


# opens csv file with input parameters of file_name
def open_csv(file_name):
    # open and read csv then store lines into 2D array "matrix"
    matrix = []
    with open(file_name) as csv_file:
        data = list(csv.reader(csv_file, delimiter=','))
        i = 0
        for col in data:
            matrix.append([])
            matrix[i].append(col)
            i += 1
    return matrix


# main function
if __name__ == '__main__':

    for i in range(len(input_files)):
        output_file = 'output'
        state_matrix = open_csv(input_files[i])  # adjacency matrix from csv file
        print("\n\n------------------------------------------------- Color States for", input_files[i], "-------------------------------------------------")
        output_file += str(i+1) + '.txt'
        ColorStates(state_matrix, output_file)
    #for i in range(len(state_matrix)):
    #    print(state_matrix[i])

    print("----- end program -----")
