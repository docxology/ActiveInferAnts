from typing import Dict, Any
import numpy as np
from InferAnts import ActiveNestmate
import config

def initialize_single_nestmate(nest_id: int, nestmates_id: int, developmental_parameters: Dict[str, Any]) -> ActiveNestmate:
    try:
        # Generate a unique position and influence factor for the nestmate
        position = np.random.choice(config.ENVIRONMENT_CONFIG['NEST_POSITIONS'])
        influence_factor = np.random.uniform(config.ANT_AND_COLONY_CONFIG['INFLUENCE_FACTOR_RANGE'][0], config.ANT_AND_COLONY_CONFIG['INFLUENCE_FACTOR_RANGE'][1])
        
        # Merge ant-specific parameters with developmental parameters
        agent_params = {
            'SENSORY_MODALITIES': config.ANT_AND_COLONY_CONFIG['SENSORY_MODALITIES'],
            'OBSERVATION_DIM': config.ANT_AND_COLONY_CONFIG['OBSERVATION_DIM'],
            'ACTION_MODALITIES': config.ANT_AND_COLONY_CONFIG['ACTION_MODALITIES'],
            'STATE_DIM': config.ANT_AND_COLONY_CONFIG['STATE_DIM'],
            **developmental_parameters,  # Incorporate developmental parameters
        }
        
        # Initialize and return a single ActiveNestmate instance
        nestmate = ActiveNestmate(position=position, influence_factor=influence_factor, **agent_params)
        return nestmate
    except KeyError as e:
        raise ValueError(f"Missing required developmental parameter: {e}")
