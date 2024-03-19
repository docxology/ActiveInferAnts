import numpy as np
from InferAnts import ActiveNestmate

def initialize_colony(nests_count, nestmates_count):
    """
    Initializes N nests with M nestmates each as ActiveInference agents.
    
    Args:
    - nests_count (int): The number of nests to initialize.
    - nestmates_count (int): The number of nestmates per nest.
    
    Returns:
    - list: A list of nests, each containing a list of ActiveNestmate instances.
    """
    nests = []
    for _ in range(nests_count):
        nestmates = []
        for _ in range(nestmates_count):
            # Assuming a simplified position and influence factor for demonstration
            position = np.random.randint(0, 100, size=2)  # Random 2D position
            influence_factor = np.random.rand()  # Random influence factor between 0 and 1
            
            # Initialize an ActiveNestmate with random parameters
            nestmate = ActiveNestmate(position=position, influence_factor=influence_factor, SENSORY_MODALITIES=5, OBSERVATION_DIM=10, ACTION_MODALITIES=3, STATE_DIM=5)
            nestmates.append(nestmate)
        nests.append(nestmates)
    return nests
