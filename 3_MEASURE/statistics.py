import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SimulationStatistics:
    def __init__(self, simulation_results):
        self.results = simulation_results
        self.agents_df = pd.DataFrame(simulation_results['agents'])
        self.food_sources_df = pd.DataFrame(simulation_results['food_sources'])
        self.nests_df = pd.DataFrame(simulation_results['nests'])

    def summary_statistics(self):
        return {
            'total_agents': len(self.agents_df),
            'total_food_sources': len(self.food_sources_df),
            'total_nests': len(self.nests_df),
            'total_food_collected': self.nests_df['food_collected'].sum(),
            'simulation_steps': self.results['simulation_steps']
        }

    def agent_type_statistics(self):
        return self.agents_df.groupby('type')['energy'].agg(['mean', 'median', 'min', 'max', 'std']).to_dict('index')

    def plot_agent_energy_distribution(self, file_path):
        sns.histplot(self.agents_df['energy'], bins=20, kde=True)
        plt.xlabel('Agent Energy')
        plt.ylabel('Count')
        plt.title('Agent Energy Distribution')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(file_path)
        plt.close()

# Example usage
# results = load_simulation_results(file_path)
# stats = SimulationStatistics(results)
# print(stats.summary_statistics())
# print(stats.agent_statistics())  
# print(stats.agent_type_statistics())
# stats.plot_agent_energy_distribution('energy_dist.png')
