class Sampling():
    """Constraints loaded from a file."""

    def __init__(self, in_file, out_file, n_results):
        """
        Construct a new object from input file

        :param in_file: Name of the input file to read the Constraint from (string)
        :param out_file: Name of the output file to write the vector data to (string)
        :param n_results: Number of vectors to output within valid space (integer)
        """
        with open(in_file, "r") as f:
            lines = f.readlines()
        # Parse the dimension from the first line
        self.n_dim = int(lines[0])
        # Parse the example from the second line
        self.example = [float(x) for x in lines[1].split(" ")[0:self.n_dim]]

        # Run through the rest of the lines and compile the constraints
        self.exprs = []
        for i in range(2, len(lines)):
            # support comments in the first line
            if lines[i][0] == "#":
                continue
            self.exprs.append(compile(lines[i], "<string>", "eval"))
        return 

    def get_example(self):
        """Get the example feasible vector"""
        return self.example

    def get_ndim(self):
        """Get the dimension of the space on which the constraints are defined"""
        return self.n_dim
 
    def get_allvectors(self):
        """Get all possible solutions of multi-dimensional constraints"""

        import numpy as np
        # Initialize location for solution lists by dimension
        self.all_solns = []

        # Find number of decimal places in each example point to determine increments of solutions for each dimension:
        for pts in range(self.n_dim):
            make_str = str(self.example[(pts)])
            index = make_str.find('.') 
            N = 10**(len(make_str[index+1:])) #increment based on decimal places
            # Generate all possible volume-fraction solutions (with values between 0 and 1) 
            #   for each dimension out to decimal place in the example feasible point. 
            self.all_solns.append(np.linspace(0,1,N))

        # Define function to evaluate the constraints for a given vector (similar to apply function in constraints.py)
        def apply_constraints(self, x):

            """
            Apply the constraints to a vector, returning True only if all are satisfied

            :param x: list or array on which to evaluate the constraints
            """
            for expr in self.exprs:
                if not eval(expr):
                    return False
            return True
 
        # Initialize location for vectors that meet constraints
        self.all_vectors = []

        # Systematically step through all possible solutions based on a combinatorics-like evaluation of all_solns array created above.
        #   Each embedded for-loop represents one dimension, with if-statements inserted to exit the loop if the file's dimensions (n_dim) have been exceeded.
        #   Within each loop, solutions from each dimension of all_solns are selected to iteratively define vectors.
        #   Each vector is only saved if it fulfills constraints using the apply_constraints function defined above. 
        #   Up to 12 dimensions are allowed.
        for dim_one in range(1,len(self.all_solns[0])): 
            for dim_two in range(1,len(self.all_solns[1])): 
                if self.n_dim == 2:
                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1]]):
                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1]])
                else:
                    for dim_three in range(1,len(self.all_solns[2])):
                        if self.n_dim == 3:
                            if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1]]):
                                self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1]])
                        else:
                            for dim_four in range(1,len(self.all_solns[3])):
                                if self.n_dim == 4:
                                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                            self.all_solns[3][dim_four-1]]):
                                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                            self.all_solns[3][dim_four-1]])
                                else:
                                    for dim_five in range(1,len(self.all_solns[4])):
                                        if self.n_dim == 5:
                                            if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                    self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1]]):
                                                self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                    self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1]])
                                        else:
                                            for dim_six in range(1,len(self.all_solns[5])):
                                                if self.n_dim == 6:
                                                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                            self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1]]):
                                                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                            self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1]])
                                                else:
                                                    for dim_seven in range(1,len(self.all_solns[6])):
                                                        if self.n_dim == 7:
                                                            if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                                    self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                    self.all_solns[6][dim_seven-1]]):
                                                                self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],self.all_solns[2][dim_three-1],
                                                                    self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                    self.all_solns[6][dim_seven-1]])
                                                        else:
                                                            for dim_eight in range(1,len(self.all_solns[7])):
                                                                if self.n_dim == 8:
                                                                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                            self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1]]):
                                                                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                            self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1]])
                                                                else:
                                                                    for dim_nine in range(1,len(self.all_solns[8])):
                                                                        if self.n_dim == 9:
                                                                            if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                    self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                                    self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                    self.all_solns[8][dim_nine-1]]):
                                                                                self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                    self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                                    self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                    self.all_solns[8][dim_nine-1]])
                                                                        else:
                                                                            for dim_ten in range(1,len(self.all_solns[9])):
                                                                                if self.n_dim == 10:
                                                                                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                                            self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                            self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1]]):
                                                                                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],self.all_solns[4][dim_five-1],
                                                                                            self.all_solns[5][dim_six-1],self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                            self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1]])
                                                                                else:
                                                                                    for dim_eleven in range(1,len(self.all_solns[10])):
                                                                                        if self.n_dim == 11:
                                                                                            if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                                    self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],
                                                                                                    self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                                                    self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                                    self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1],
                                                                                                    self.all_solns[10][dim_eleven-1]]):
                                                                                                self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                                    self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],
                                                                                                    self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                                                    self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                                    self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1],
                                                                                                    self.all_solns[10][dim_eleven-1]])
                                                                                        else:
                                                                                            for dim_twelve in range(1,len(self.all_solns[11])):
                                                                                                if self.n_dim == 12:
                                                                                                    if apply_constraints(self, [self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],
                                                                                                            self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                                                            self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                                            self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1],
                                                                                                            self.all_solns[10][dim_eleven-1],self.all_solns[11][dim_twelve-1]]):
                                                                                                        self.all_vectors.append([self.all_solns[0][dim_one-1],self.all_solns[1][dim_two-1],
                                                                                                            self.all_solns[2][dim_three-1],self.all_solns[3][dim_four-1],
                                                                                                            self.all_solns[4][dim_five-1],self.all_solns[5][dim_six-1],
                                                                                                            self.all_solns[6][dim_seven-1],self.all_solns[7][dim_eight-1],
                                                                                                            self.all_solns[8][dim_nine-1],self.all_solns[9][dim_ten-1],
                                                                                                            self.all_solns[10][dim_eleven-1],self.all_solns[11][dim_twelve-1]])
                                                                                                else:
                                                                                                    print('Maximum dimensions allowed = 12')      

    def get_nresults_solns(self, out_file, n_results):
        """ Identify n_results number of evenly-dispersed vector solutions and write to output file 

        :param out_file: Name of the output file to write the vector data to (string)
        :param n_results: Number of vectors to output within valid space (integer)
        """

        # Define the number of solutions generated (n_solutions) 
        self.n_solutions = len(self.all_vectors)
        # Define the number of solutions requested (n_results) 
        self.n_results = n_results
        # Initialize locations for evenly-space query points (res_locations) and vectors to write to output file (output_vectors)
        self.res_locations = []
        self.output_vectors = []

        import numpy as np
        import math 

        # If-statement tests whether the solution set needs to be paired down to the number of requested vectors.  
        if self.n_solutions > self.n_results:
            # Define evenly-spaced query points within the solution set 
            self.res_locations = np.linspace(1,self.n_solutions,self.n_results)

            for location in range(1,len(self.res_locations)):  
             # Step through self.res_locations and pull out the vectors for self.n_solutions at query points
                self.output_vectors.append(self.all_vectors[math.floor(self.res_locations[location-1])])
        else:
            self.output_vectors = self.all_vectors

        # Write solutions to output file. 
        with open(out_file, "w") as file_object:
            for line in range(1,len(self.output_vectors)):
                file_object.write(" ".join([str(num) for num in self.output_vectors[line-1]]))
                file_object.write("\n")


# Input parameters here:
in_file = 'example.txt' 
out_file = 'out.txt' 
n_results = 1000

# Run class here:
mixture =  Sampling(in_file, out_file, n_results)
Sampling.get_ndim(mixture)
Sampling.get_allvectors(mixture)
Sampling.get_nresults_solns(mixture, out_file, n_results)