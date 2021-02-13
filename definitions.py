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

class Environment():
    """
        Implements the interface for an Environment 
    """

    def initial_percepts(self):
        """
        Returns the environment initial percepts
        
        Raises: 
            NotImplementedError: If the method is not implemented or not overridden
        """
        raise NotImplementedError('initial_percepts')
    
    def signal(self, action):
        """
        Returns the environment percepts after action is executed
        
        Raises: 
            NotImplementedError: If the method is not implemented or not overridden
        """
        raise NotImplementedError('signal')