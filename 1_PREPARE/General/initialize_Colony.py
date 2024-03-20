import numpy as np
from InferAnts import ActiveNestmate
import config
import metaconfig

def initialize_colony(nests_count, nestmates_count):
    nests = []
    for _ in range(nests_count):
        nestmates = []
        for _ in range(nestmates_count):
            # Use environment configuration for realistic positioning
            position = np.random.choice(config.ENVIRONMENT_CONFIG['NEST_POSITIONS'])
            influence_factor = np.random.uniform(config.ANT_AND_COLONY_CONFIG['INFLUENCE_FACTOR_RANGE'][0], config.ANT_AND_COLONY_CONFIG['INFLUENCE_FACTOR_RANGE'][1])
            
            # Initialize ActiveNestmate with enhanced parameters from metaconfig
            agent_params = {
                'SENSORY_MODALITIES': metaconfig.ACTIVE_INFERENCE['SENSORY_MODALITIES'],
                'OBSERVATION_DIM': metaconfig.ACTIVE_INFERENCE['OBSERVATION_DIM'],
                'ACTION_MODALITIES': metaconfig.ACTIVE_INFERENCE['ACTION_MODALITIES'],
                'STATE_DIM': metaconfig.ACTIVE_INFERENCE['STATE_DIM'],
                # Additional parameters can be added here
            }
            nestmate = ActiveNestmate(position=position, influence_factor=influence_factor, **agent_params)
            nestmates.append(nestmate)
        nests.append(nestmates)
    return nests
