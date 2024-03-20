import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SimulationRenderer:
    def __init__(self, simulation_environment, nests, agents):
        self.simulation_environment = simulation_environment
        self.nests = nests
        self.agents = agents
        self.fig, self.ax = plt.subplots()
    
    def setup_environment(self):
        """Initial setup of the simulation environment for visualization."""
        self.ax.clear()
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title('Simulation Initialization')
        # Plot nests
        for nest in self.nests:
            self.ax.plot(nest.x, nest.y, 'ro')  # Represent nests with red dots
        # Plot initial positions of agents
        for agent in self.agents:
            self.ax.plot(agent.x, agent.y, 'bo')  # Represent agents with blue dots
    
    def update_visualization(self, frame):
        """Dynamic visualization updated during the simulation."""
        self.ax.clear()
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title(f'Simulation Step: {frame}')
        # Update positions of agents
        for agent in self.agents:
            self.ax.plot(agent.x, agent.y, 'bo')  # Update agent positions
    
    def animate_simulation(self, steps):
        """Create an animation representing the simulation over time."""
        anim = animation.FuncAnimation(self.fig, self.update_visualization, frames=steps, interval=100)
        plt.show()
    
    def render_post_simulation(self, simulation_results):
        """Detailed visualization after the simulation has concluded."""
        self.ax.clear()
        self.ax.set_title('Post-Simulation Analysis')
        # Example: Plot trajectories or summarize behaviors
        # This is a placeholder for post-simulation visualization logic
        plt.show()
