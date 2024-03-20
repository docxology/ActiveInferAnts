import time
from render_Simulation import SimulationRenderer
from situational_Antwareness import visualize_agent_internals
from plan_Simulation import plan_simulation

class SimulationExecutor:
    def __init__(self):
        self.simulation = plan_simulation()
        self.renderer = SimulationRenderer(
            self.simulation.simulation_environment, 
            self.simulation.nests, 
            self.simulation.agents
        )
    
    def setup_environment(self):
        self.renderer.setup_environment()
    
    def execute_steps(self):
        for step in range(self.simulation.simulation_environment.max_steps):
            self.simulation.update()
            self.optional_visualization(step)
            self.renderer.update_visualization(step)
            time.sleep(0.1)  # Real-time progression delay
    
    def optional_visualization(self, step):
        if step % 100 == 0:  # Visualize every 100 steps
            for agent in self.simulation.agents:
                visualize_agent_internals(agent)
    
    def post_simulation(self):
        self.renderer.render_post_simulation(self.simulation.collect_results())
        print("Simulation completed. Results are ready for analysis.")
    
    def run(self):
        self.setup_environment()
        self.execute_steps()
        self.post_simulation()

if __name__ == "__main__":
    executor = SimulationExecutor()
    executor.run()

