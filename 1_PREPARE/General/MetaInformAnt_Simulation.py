# pymdp_ants.py

import numpy as np
from pymdp.agent import Agent
from ant_multimodal import Ant, FoodSource, Environment, Niche
import config
import metaconfig  # Importing the metaconfig for additional configurations

# Define the MetaInformAnt simulation framework with enhanced features
class MetaInformAntSimulation:
    def __init__(self, num_agents, simulation_environment, num_food_sources, num_nests, agent_params, niche_params):
        self.num_agents = num_agents
        self.simulation_environment = simulation_environment
        self.num_food_sources = num_food_sources
        self.num_nests = num_nests
        self.agent_params = agent_params  # Storing agent parameters
        self.niche_params = niche_params  # Storing niche parameters
        self.agents = self._initialize_agents()
        self.food_sources = self._initialize_food_sources()
        self.nests = self._initialize_nests()
        
    def _initialize_agents(self):
        agents = []
        for _ in range(self.num_agents):
            # Utilizing the INITIAL_POSITIONS from config.py for agent creation
            initial_positions = config.ANT_AND_COLONY_CONFIG['COLONY']['INITIAL_POSITIONS']['XYZ']
            # Including agent parameters in agent creation
            agent = Ant.create(initial_positions['X'], initial_positions['Y'], config.ANT_AND_COLONY_CONFIG['COLONY']['INFLUENCE_FACTOR'], **self.agent_params)
            agents.append(agent)
        return agents
    
    def _initialize_food_sources(self):
        food_sources = []
        for _ in range(self.num_food_sources):
            # Randomly selecting a resource zone from config.py for food source initialization
            resource_zone = np.random.choice(config.ENVIRONMENT_CONFIG['RESOURCE_ZONES'])
            # Including niche parameters in food source creation
            food_source = FoodSource.create(resource_zone['POSITION']['X'], resource_zone['POSITION']['Y'], **self.niche_params)
            food_sources.append(food_source)
        return food_sources
    
    def _initialize_nests(self):
        nests = []
        for _ in range(self.num_nests):
            # Randomly selecting a position for nest initialization
            x_position = np.random.randint(0, config.ENVIRONMENT_CONFIG['GRID']['WIDTH'])
            y_position = np.random.randint(0, config.ENVIRONMENT_CONFIG['GRID']['HEIGHT'])
            # Including niche parameters in nest creation
            nest = Niche.create(x_position, y_position, config.ANT_AND_COLONY_CONFIG['COLONY']['INFLUENCE_FACTOR'], **self.niche_params)
            nests.append(nest)
        return nests
    
    def execute_simulation(self, simulation_steps):
        for step in range(simulation_steps):
            for agent in self.agents:
                # Sensory perception phase
                pheromone_obs, vision_obs, tactile_obs, sound_obs, food_obs = self.simulation_environment.collect_observations(agent, self.food_sources, self.nests)
                agent.process_observations(pheromone_obs, vision_obs, tactile_obs, sound_obs, food_obs)
                
                # Decision-making and action phase  
                chosen_action = agent.decide_next_action()
                self.simulation_environment.apply_agent_action(agent, chosen_action)
                
                # Check for food collection and nest interactions
                self.simulation_environment.check_food_collection(agent, self.food_sources)
                self.simulation_environment.check_nest_interaction(agent, self.nests)

# Entry point for the simulation
def run_simulation():
    simulation_environment = Environment()  # Assume Environment class is implemented elsewhere
    
    # Extracting agent and niche parameters from metaconfig
    agent_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['AGENT_PARAMS']
    niche_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['NICHE_PARAMS']
    
    meta_inform_ant_simulation = MetaInformAntSimulation(config.SIMULATION_SETTINGS['AGENT_COUNT'], simulation_environment, config.SIMULATION_SETTINGS['FOOD_SOURCE_COUNT'], config.SIMULATION_SETTINGS['NEST_COUNT'], agent_params, niche_params)
    meta_inform_ant_simulation.execute_simulation(simulation_steps=config.SIMULATION_SETTINGS['MAX_STEPS'])

if __name__ == "__main__":
    run_simulation()

