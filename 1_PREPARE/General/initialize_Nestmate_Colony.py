import numpy as np
from InferAnts import ActiveNestmate
from typing import List, Dict, Any, Tuple
import config
import metaconfig

def initialize_colony(nest_count: int, agent_count_per_nest: int, env_config: Dict[str, Any], ant_config: Dict[str, Any], meta_config: Dict[str, Any]) -> List[List[ActiveNestmate]]:
    colony = [initialize_nest(nest_id, agent_count_per_nest, env_config, ant_config, meta_config) for nest_id in range(nest_count)]
    return colony

def initialize_nest(nest_id: int, agent_count: int, env_config: Dict[str, Any], ant_config: Dict[str, Any], meta_config: Dict[str, Any]) -> List[ActiveNestmate]:
    positions = np.random.choice(env_config['NEST_POSITIONS'], size=agent_count)
    nestmates = [initialize_single_nestmate(nest_id, nestmate_id, generate_developmental_parameters(), position, ant_config, meta_config) for nestmate_id, position in enumerate(positions)]
    return nestmates

def initialize_single_nestmate(nest_id: int, nestmate_id: int, developmental_parameters: Dict[str, Any], position: Tuple[int, int], ant_config: Dict[str, Any], meta_config: Dict[str, Any]) -> ActiveNestmate:
    influence_factor = np.random.uniform(*ant_config['INFLUENCE_FACTOR_RANGE'])
    agent_params = {**meta_config['ACTIVE_INFERENCE'], **developmental_parameters}
    nestmate = ActiveNestmate(position=position, influence_factor=influence_factor, **agent_params)
    return nestmate

def generate_developmental_parameters() -> Dict[str, Any]:
    return {
        'growth_rate': np.random.uniform(0.1, 1.0),
        'exploration_tendency': np.random.choice(['low', 'medium', 'high']),
    }
``
 