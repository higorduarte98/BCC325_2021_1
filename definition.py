class Agent():
    """
        Implements the interface for an Agent
    """

    def __init__(self, env):
        """
        Contructor for the agent class

        Args:
            env: a reference to an enviroment
            
        """
        self.env = env
    
    def act(self):
        """
        Defines the agent action

        Raises:
            NotImplementedError: If the method is not implemented or not overrided

        """
        
        raise NotImplementedError('act')