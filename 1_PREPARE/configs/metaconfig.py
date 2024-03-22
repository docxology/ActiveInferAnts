import numpy as np

# Consolidated Meta-Configuration for Simulation, Active Inference, and Ant & Colony
META_CONFIG = {
    'SIMULATION': {
        'MAX_STEPS_RANGE': (100, 1000),  # Range for maximum number of steps per simulation
        'AGENT_COUNT_RANGE': (50, 500),  # Range for total number of agents
        'NEST_COUNT_RANGE': (1, 10),  # Range for total number of nests
        'PARALLEL_EXECUTION_OPTIONS': [True, False],  # Options for enabling/disabling parallel execution
        'WORKER_COUNT_RANGE': (1, 8),  # Range for number of workers in parallel execution
        'PARALLELIZATION_STRATEGIES': ['distributed', 'multithreading'],  # Available parallelization strategies
        'COMPUTATION': {
            'GPU_ACCELERATION_OPTIONS': [True, False],  # Options for enabling/disabling GPU acceleration
            'GPU_PREFERENCE_OPTIONS': ['high_performance', 'energy_saving'],  # Preferred GPU modes
            'DISTRIBUTED_COMPUTING_OPTIONS': [True, False],  # Options for enabling/disabling distributed computing
            'CLUSTER_NODE_COUNT_RANGE': (2, 16),  # Range for number of nodes in the computing cluster
            'COMMUNICATION_PROTOCOLS': ['MPI', 'TCP/IP'],  # Protocols used for communication in distributed computing
        },
    },
    'ACTIVE_INFERENCE': {
        'INFERENCE_MODEL_OPTIONS': ['variational', 'predictive_coding', 'bayesian_filtering', 'deep_active_inference', 'ensemble_methods'],
        'PLANNING_HORIZON': {
            'TYPE_OPTIONS': ['fixed', 'adaptive'],
            'FIXED_RANGE': (5, 30),
            'ADAPTIVE_STRATEGY_OPTIONS': ['contextual_complexity'],
        },
        'ADAPTIVE_LEARNING': {
            'ENABLED': [True, False],
            'LEARNING_RATE_RANGE': (0.01, 0.5),
            'FEEDBACK_SENSITIVITY_OPTIONS': ['fixed', 'adaptive'],
            'MODEL_UPDATING_OPTIONS': ['online', 'batch'],
        },
        'CONTEXT_AWARENESS': {
            'ENABLED_OPTIONS': [True, False],
            'DYNAMIC_ADJUSTMENT_OPTIONS': [True, False],
            'PREDICTION': [True, False],
            'CONTEXT_INTEGRATION_STRATEGIES': ['multimodal', 'unimodal'],
        },
        'PRECISION_WEIGHTING': {
            'PERCEPTION_RANGE': (0.1, 1.0),
            'ACTION_RANGE': (0.1, 1.0),
            'ADAPTIVE': [True, False],
        },
        'TIME_RESOLUTION_OPTIONS': ['discrete', 'continuous'],  # Available time resolution options
        'PRECISION_WEIGHTING_RANGE': (0.1, 1.0),  # Range for precision weighting
        'GENERALIZATION_DEPTH_RANGE': (1, 10),  # Range for generalization depth
        'ITERATION_LIMIT_RANGE': (10, 50),  # Range for iteration limit
        'LEARNING_RATE_RANGE': (0.01, 0.5),  # Range for learning rate
        'FEEDBACK_SENSITIVITY_OPTIONS': ['fixed', 'adaptive'],  # Available feedback sensitivity options
        'MODEL_UPDATING_OPTIONS': ['online', 'batch'],  # Available model updating strategies
        'CONTEXT_TYPES': ['environmental', 'social', 'temporal', 'emotional'],  # Available context types
        'COGNITIVE_COMPLEXITY_TYPES': ['simple', 'complex', 'hierarchical', 'emergent', 'adaptive'],  # Available cognitive complexity types
        'GOAL_TYPES': ['survival', 'exploration', 'social_interaction'],  # Available goal types
        'EXPECTATION_FREE_ENERGY_OPTIONS': [True, False],  # Options for enabling/disabling calculation of expected free energy
    },
    'ANT_AND_COLONY': {
        'MOVEMENT_OPTIONS': [
            [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)],  # 8-directional movement
            [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)],  # 4-directional movement
        ],
        'PHEROMONE_TYPE_RANGE': (1, 10),  # Range for number of pheromone types
        'MAX_PHEROMONE_RELEASE_RATE_RANGE': (1, 10),  # Range for maximum pheromone release rate
        'SOUND_PRODUCTION_TYPES': [['stridulation', 'sing', 'talk', 'grunt'], ['stridulation', 'sing']],  # Available sound production types
        'SOUND_INTENSITY_LEVEL_RANGE': (1, 10),  # Range for sound intensity levels
        'PERCEPTUAL_FIELD_SIZE_RANGE': (1, 7),  # Range for perceptual field size
        'MEMORY_CAPACITY_RANGE': (50, 200),  # Range for memory capacity
        'ATTENTION_SPAN_RANGE': (3, 10),  # Range for attention span
        'DECISION_STRATEGY_OPTIONS': ['deterministic', 'probabilistic'],  # Available decision-making strategies
        'RISK_TAKING_OPTIONS': ['low', 'moderate', 'high'],  # Expanded risk-taking options
        'COLONY_STRUCTURE_OPTIONS': ['subterranean', 'arboreal', 'mixed'],  # Types of nest structures
        'FORAGING_STRATEGIES': ['random_search', 'pheromone_trail', 'visual_cues'],  # Expanded foraging strategies
        'COMMUNICATION_METHODS': ['pheromones', 'tactile', 'auditory', 'visual'],  # Expanded communication methods within the colony
        'DEFENSE_MECHANISMS': ['chemical', 'physical', 'camouflage'],  # Expanded defense mechanisms employed
        'EXPANSION_STRATEGY_OPTIONS': ['gradual', 'rapid', 'steady'],  # Options for colony expansion strategies
        'THREAT_RESPONSES': ['evacuation', 'defense', 'hide', 'counterattack'],  # Expanded threat responses
    },
}
