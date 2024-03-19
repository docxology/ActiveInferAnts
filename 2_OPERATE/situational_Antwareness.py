def visualize_agent_internals(agent):
    """
    Visualize the internal state of an ActiveInferenceAgent or its subclasses.
    This method prints out a verbose summary of all instantiated variables, including
    the total number of variables, their sizes, and detailed descriptions.
    """
    print("Visualizing Agent Internals in Verbose Mode:")
    print(f"Position: {agent.position} (The current position of the agent in the environment)")
    print(f"Influence Factor: {agent.influence_factor} (A measure of the agent's influence on its surroundings)")
    print(f"Agent Parameters: {agent.agent_params} (A dictionary of agent-specific parameters)")
    
    # Calculate the total number of variables and their sizes
    total_variables = 4  # Position, Influence Factor, Agent Params, and 4 matrices
    total_size = 0  # Initialize total size
    
    # Calculate size of A, B, C, D matrices
    a_size = agent.A_matrix.size
    b_size = agent.B_matrix.size
    c_size = agent.C_matrix.size
    d_size = agent.D_matrix.size
    
    total_size += a_size + b_size + c_size + d_size  # Sum up the sizes
    
    print("Matrices Detailed Information:")
    print(f"A Matrix: Shape {agent.A_matrix.shape}, Size {a_size} (Sensory modalities mapping to observations)")
    print(f"B Matrix: Shape {agent.B_matrix.shape}, Size {b_size} (Action modalities mapping to state transitions)")
    print(f"C Matrix: Shape {agent.C_matrix.shape}, Size {c_size} (Preferences over observations)")
    print(f"D Matrix: Shape {agent.D_matrix.shape}, Size {d_size} (Prior beliefs over initial states)")
    
    print(f"Total Number of Variables: {total_variables} (Including position, influence factor, agent parameters, and matrices)")
    print(f"Total Size of Variables: {total_size} (Sum of sizes of all variables)")

    # Additional details for NESTMATE and COLONY levels
    if isinstance(agent, ActiveNestmate):
        print("NESTMATE Specific Information:")
        print(f"Nestmate Config: {agent.nestmate_config} (Configuration specific to nestmates)")
    elif isinstance(agent, ActiveColony):
        print("COLONY Specific Information:")
        print(f"Colony Config: {agent.colony_config} (Configuration specific to colonies)")
