import numpy as np
from MetaInformAnt_Simulation import MetaInformAntSimulation
import config
import metaconfig

def plan_simulation():
    # Extract simulation settings from configuration
    simulation_environment = Environment()  # Assuming Environment class is implemented
    agent_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['AGENT_PARAMS']
    niche_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['NICHE_PARAMS']
    
    # Initialize the MetaInformAntSimulation with parameters from the config
    simulation = MetaInformAntSimulation(
        num_agents=config.SIMULATION_SETTINGS['AGENT_COUNT'],
        simulation_environment=simulation_environment,
        num_food_sources=config.SIMULATION_SETTINGS['FOOD_SOURCE_COUNT'],
        num_nests=config.SIMULATION_SETTINGS['NEST_COUNT'],
        agent_params=agent_params,
        niche_params=niche_params
    )
    
    # Pre-simulation rendering
    render_pre_simulation(simulation_environment, simulation.nests, simulation.food_sources)
    
    # Execute the simulation with rendering
    simulation.execute_simulation(simulation_steps=config.SIMULATION_SETTINGS['MAX_STEPS'], render_callback=render_during_simulation)
    
    # Post-simulation rendering
    render_post_simulation(simulation.get_results())

if __name__ == "__main__":
    plan_simulation()
