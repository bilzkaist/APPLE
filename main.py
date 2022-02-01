#*****************************************************************************
#
#  APPLE: Accelerating Particle filter for Positioning and Localization Estimation Code.
#                             Written  by Bilal Dastagir & Omer Tariq.
#                                Feb, 1st, 2022
#
#******************************************************************************

#FOLDERPATH =  "/Users/bilaldastagir/Documents/vscode/APPLE/APPLE"
import sys

sys.path.append('/Users/bilaldastagir/Documents/vscode/APPLE/APPLE/')

# Simulation + plotting requires a robot, visualizer and world
#from simulator import Robot, Visualizer, World

# Supported resampling methods (resampling algorithm enum for SIR and SIR-derived particle filters)
from system.resampling.resampler import ResamplingAlgorithms

# Particle filters
from system.particle_filters.particle_filter_sir import ParticleFilterSIR



#Global Variables 
BETA = [0]
ALPHA = [1]
BRAVO  = [2]
CHARLIE = [3]

def run_beta():
    print("Beta Program is Started........... !!!")
    # Write code Here
    print("System Path = ",sys.path)
    print("Beta Program is Ended Successfully !!!")
    return BETA

def run_alpha():
    print("Alpha Program is Started........... !!!")
    # Write code Here
    print("Alpha Program is Ended Successfully !!!")
    return ALPHA
    

def run_bravo():
    print("Bravo Program is Started........... !!!")
    # Write code Here
    print("Bravo Program is Ended Successfully !!!")
    return BRAVO

def run_charlie():
    print("Charlie Program is Started........... !!!")
    # Write code Here
    print("Charlie Program is Ended Successfully !!!")
    return CHARLIE
    
def switch_mode(mode):
    # Program Started
    switcher = {
        0: run_beta,
        1: run_alpha,
        2: run_bravo,
        3: run_charlie
        
        
    }
     # Get the function from switcher dictionary
    func = switcher.get(mode, lambda: "Invalid mode")
    # Execute the function
    print("Mode Selected : ",func())
    # Program Ended 

def run():
    print("......................Main Program is Started........... !!!\n")
    # write coode here
    runMode = BETA
    if (runMode == ALPHA):
        run_alpha()
    else:
        run_beta()
        
    print("\n......................Main Program is Ended Successfully !!!")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_bye(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(' Bilal Dastagir')
    run()
    print_bye('Bilal Dastagir')