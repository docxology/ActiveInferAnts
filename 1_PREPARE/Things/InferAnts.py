import numpy as np
import config
from typing import Dict, Any, Callable
from scipy.stats import entropy

class ActiveInferenceAgent:
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        """
        Initialize an active inference agent with specified parameters and matrices.

        :param position: Initial position of the agent in a numpy array.
        :param influence_factor: Influence factor for agent's actions as a float.
        :param agent_params: Additional parameters for agent configuration as a dictionary.
        """
        self.position = position
        self.influence_factor = influence_factor
        self.agent_params = agent_params
        self.A_matrix = self._initialize_matrix('A_matrix_config', self.agent_params.get('SENSORY_MODALITIES'), self.agent_params.get('OBSERVATION_DIM'))
        self.B_matrix = self._initialize_matrix('B_matrix_config', self.agent_params.get('ACTION_MODALITIES'), self.agent_params.get('STATE_DIM'), self.agent_params.get('STATE_DIM'))
        self.C_matrix = self._initialize_matrix('C_matrix_config', self.agent_params.get('OBSERVATION_DIM'))
        self.D_matrix = self._initialize_matrix('D_matrix_config', self.agent_params.get('STATE_DIM'))

    def _initialize_matrix(self, config_key: str, *dims):
        """
        Initialize a matrix based on configuration or default to zeros.

        :param config_key: Configuration key for the matrix.
        :param dims: Dimensions for the matrix.
        :return: A numpy array representing the initialized matrix.
        """
        return self.agent_params.get(config_key, np.zeros(dims))

    def perceive(self, observations: np.ndarray):
        """
        Update agent's beliefs based on new observations.

        :param observations: New sensory observations as a numpy array.
        """
        prediction_error = self.agent_params.get('perception_strategy', lambda obs, agent: obs - agent._predict_sensory_outcomes())(observations, self)
        self._update_beliefs(prediction_error)

    def _predict_sensory_outcomes(self) -> np.ndarray:
        """
        Predict sensory outcomes based on the agent's current position.

        :return: A numpy array of predicted sensory outcomes.
        """
        return np.dot(self.A_matrix, self.position)

    def _update_beliefs(self, prediction_error: np.ndarray):
        """
        Update the agent's position based on the prediction error.

        :param prediction_error: Prediction error as a numpy array.
        """
        self.position -= self.influence_factor * prediction_error

    def calculate_vfe(self, observation: np.ndarray) -> float:
        """
        Calculate the Variational Free Energy for a given observation.

        :param observation: Observation as a numpy array.
        :return: Variational Free Energy as a float.
        """
        qs = self._approximate_posterior(observation)
        expected_log_likelihood = np.sum(qs * np.log(self.A_matrix[:, observation]))
        kl_divergence = np.sum(qs * (np.log(qs) - np.log(self.position)))
        vfe = -(expected_log_likelihood - kl_divergence)
        return vfe

    def calculate_efe(self, action: np.ndarray, future_states: np.ndarray, preferences: np.ndarray, uncertainty: float) -> float:
        """
        Calculate the Expected Free Energy for a given action.

        :param action: Action as a numpy array.
        :param future_states: Future states as a numpy array.
        :param preferences: Preferences as a numpy array.
        :param uncertainty: Uncertainty as a float.
        :return: Expected Free Energy as a float.
        """
        pragmatic_value = np.sum(future_states * (np.log(future_states) - np.log(preferences)))
        epistemic_value = entropy(future_states)
        efe = pragmatic_value + epistemic_value
        return efe

    def decide_next_action(self) -> np.ndarray:
        """
        Decide the next action based on Expected Free Energy scores.

        :return: The chosen action as a numpy array.
        """
        possible_actions = self._generate_possible_actions()
        efe_scores = np.array([self.calculate_efe(action) for action in possible_actions])
        return possible_actions[np.argmin(efe_scores)]

    def update_internal_states(self, action: np.ndarray, observation: np.ndarray):
        """
        Update the agent's internal states based on action and observation.

        :param action: Action taken by the agent as a numpy array.
        :param observation: New observation received as a numpy array.
        """
        self._update_action_model(action, observation)
        self._update_observation_model(observation)

    def _update_action_model(self, action: np.ndarray, observation: np.ndarray):
        """
        Update the action model based on the taken action and new observation.

        :param action: Action taken by the agent as a numpy array.
        :param observation: New observation received as a numpy array.
        """
        self.B_matrix += np.outer(action, observation)

    def _update_observation_model(self, observation: np.ndarray):
        """
        Update the observation model based on the new observation.

        :param observation: New observation received as a numpy array.
        """
        self.A_matrix += np.outer(observation, observation)

    def move(self, direction: np.ndarray):
        """
        Update the agent's position based on the chosen direction.

        :param direction: Direction to move in as a numpy array.
        """
        self.position += direction

    def release_pheromone(self, type: str, rate: float):
        """
        Release pheromone of a specified type at a specified rate.

        :param type: Type of pheromone as a string.
        :param rate: Rate of pheromone release as a float.
        """
        pass

    def produce_sound(self, type: str, intensity: float):
        """
        Produce sound of a specified type with a specified intensity.

        :param type: Type of sound as a string.
        :param intensity: Intensity of the sound as a float.
        """
        pass

class ActiveColony(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.colony_config = config.ANT_AND_COLONY_CONFIG['COLONY']

class ActiveNestmate(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.nestmate_config = config.ANT_AND_COLONY_CONFIG['NESTMATE']
