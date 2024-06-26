import numpy as np
from typing import List, Optional, Dict, Any
from tabulate import tabulate  # Import tabulate for table formatting
from termcolor import colored  # Import termcolor for coloring text

class NestmateAgent:
    """
    An agent that employs active inference for decision-making within an ant colony, leveraging a comprehensive model of its environment and nestmate dynamics, based on a partially-observable Markov decision process (POMDP).
    """
    def __init__(self, num_observations: List[int], num_states: List[int], num_actions: List[int], policy_length: int = 1, inference_depth: int = 1):
        """
        Initializes the NestmateAgent with dimensions for the environment, nestmate dynamics, and its preferences, aligning with the constructs of an Active Inference POMDP.
        """
        self.observation_model = [np.random.dirichlet(np.ones(num_state), num_obs) for num_obs, num_state in zip(num_observations, num_states)]  # Dirichlet distributions for observation probabilities
        self.transition_model = [np.random.dirichlet(np.ones(num_state), num_state) for num_state in num_states]  # Dirichlet distributions for state transitions
        self.preference_model = [np.eye(num_obs) for num_obs in num_observations]  # Identity matrices for preferences
        
        self.initial_state_distribution = [np.random.dirichlet(np.ones(num_state)) for num_state in num_states]  # Dirichlet distributions for initial state beliefs
        
        self.policy_prior = np.log(np.random.dirichlet(np.ones(np.prod(num_actions) ** policy_length)))  # Log probabilities for policy priors
        
        self.generative_model = {
            'observation_model': self.observation_model,
            'transition_model': self.transition_model,
            'preference_model': self.preference_model,
            'initial_state_distribution': self.initial_state_distribution,
            'policy_prior': self.policy_prior
        }
        
        self.model_dimensions = {
            'num_observations': num_observations,
            'num_states': num_states,
            'num_modalities': len(num_observations),
            'num_factors': len(num_states)
        }

        self.posterior_states = [np.copy(dist) for dist in self.initial_state_distribution]
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = list(range(len(num_states)))
        self.possible_policies = self._generate_possible_policies(num_actions)

        self._output_variable_shapes()

    def _generate_possible_policies(self, num_actions: List[int]) -> np.ndarray:
        """
        Enumerates all possible policies, considering the action space and policy length, to summarize the total number of feasible policies.
        """
        action_combinations = [np.array(range(n)) for n in num_actions]
        policy_space = np.array(np.meshgrid(*action_combinations)).T.reshape(-1, len(num_actions))
        num_policies = np.prod([len(n) ** self.policy_length for n in action_combinations])
        possible_policies = np.array(np.meshgrid(*[policy_space for _ in range(self.policy_length)])).T.reshape(-1, self.policy_length, len(num_actions))

        print(f"Total number of possible policies: {num_policies}")
        return possible_policies

    def _output_variable_shapes(self) -> None:
        """
        Outputs the shape/size of each instantiated variable to the terminal, including detailed descriptions of their roles, relationships, and generation methods, formatted as a table with coloring for readability.
        """
        headers = ["Variable", "Shape", "Description"]
        variable_shapes = [
            ['observation_model', [model.shape for model in self.observation_model], 'Dirichlet distributions representing the probability of observing each state for each observation modality.'],
            ['transition_model', [model.shape for model in self.transition_model], 'Dirichlet distributions representing the probability of transitioning from one state to another for each state factor.'],
            ['preference_model', [model.shape for model in self.preference_model], 'Identity matrices representing the agent\'s preferences over observations.'],
            ['initial_state_distribution', [model.shape for model in self.initial_state_distribution], 'Dirichlet distributions representing the agent\'s initial beliefs about the world.'],
            ['policy_prior', self.policy_prior.shape, 'Log probabilities representing the prior probabilities of each possible policy.'],
            ['possible_policies', self.possible_policies.shape, 'All feasible sequences of actions generated by enumerating all combinations of actions across the specified policy length.']
        ]
        # ASCII art-type separators for readability
        print("============================================================")
        print(colored(tabulate(variable_shapes[:2], headers=headers, tablefmt="fancy_grid"), 'cyan'))  # Models in cyan
        print("============================================================")
        print(colored(tabulate(variable_shapes[2:4], headers=headers, tablefmt="fancy_grid"), 'yellow'))  # Preferences and beliefs in yellow
        print("============================================================")
        print(colored(tabulate(variable_shapes[4:], headers=headers, tablefmt="fancy_grid"), 'green'))  # Policies in green
        print("============================================================")
        print(colored(f"Policy length: {self.policy_length}, representing the time horizon for policy inference, with each policy generated by considering all possible action sequences.", 'magenta'))
        print(colored(f"Inference depth: {self.inference_depth}, indicating the depth of recursive inference for state estimation, based on the generative model.", 'magenta'))

def main():
    # Define configurations for different scenarios
    scenarios = [
        ([1], [1], [2], 2),
        ([1], [1], [7], 2),
        # ([2], [1], [2], 1),
        # ([1], [2], [2], 1)
    ]

    for num_observations, num_states, num_actions, policy_length in scenarios:
        scenario_description = f"In this scenario, the agent navigates an environment with {len(num_observations)} observation modality(ies), {len(num_states)} hidden state(s), {len(num_actions)} affordance(s), and a decision-making horizon of {policy_length} timestep(s). This setup challenges the agent to infer the best course of action given its understanding of the world and its preferences."
        print(f"\n{scenario_description}")
        agent = NestmateAgent(num_observations, num_states, num_actions, policy_length, inference_depth=1)
        # agent._output_variable_shapes()

if __name__ == "__main__":
    main()

