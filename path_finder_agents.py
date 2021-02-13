from definitions import Agent
import numpy as np
from scipy.spatial import distance

class RandAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            # Select random neighbor
            visit = viable_neighbors[np.random.randint(0,len(viable_neighbors))]
            
            # Append neighbor to the path and add it to the frontier
            self.frontier = [path + [visit]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class BFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            for neighbor in viable_neighbors: 
                exist = False
                    
                # Multiple-Path Pruning
                exist = False

                for node in self.visited:
                    if (node == neighbor).all():
                        exist = True
                        break
                
                # If node is not in self.visited
                if exist == False:    
                    # Append neighbor to the path and add it to the frontier
                    self.frontier = self.frontier + [path + [neighbor]]
          
    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class DFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            for neighbor in viable_neighbors:            
                # Append neighbor to the path and add it to the frontier

                # Multiple-Path Pruning
                exist = False

                for node in self.visited:
                    if (node == neighbor).all():
                        exist = True
                        break
                
                # If node is not in self.visited
                if exist == False:       
                    self.frontier = [path + [neighbor]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()

        print(self.percepts['current_position'])

class GreedyAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        cost = 999999
        j = 0
        k = 0

        for i in self.frontier:
            if distance.euclidean(i[-1], self.percepts['target']) < cost:
                j=k
                cost = distance.euclidean(i[-1], self.percepts['target'])
            k = k+1

        # Path with the lowest value of heuristic function of frontier
        path = self.frontier.pop(j)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            for neighbor in viable_neighbors:            

                # Multiple-Path Pruning
                exist = False

                for node in self.visited:
                    if (node == neighbor).all():
                        exist = True
                        break
                
                # If node is not in self.visited
                if exist == False:
                    self.frontier = [path + [neighbor]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()

        print(self.percepts['current_position'])

class AStarAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        self.cost = [0]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        cost = 999999
        j = 0
        k = 0

        for i in self.frontier:
            if self.cost[k] + distance.euclidean(i[-1], self.percepts['target']) < cost:
                j=k
                cost = self.cost[k] + distance.euclidean(i[-1], self.percepts['target'])
            k = k+1

         # Path with the lowest value of cost + heuristic function of frontier
        path = self.frontier.pop(j)
        cost = self.cost.pop(j)
        
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            for neighbor in viable_neighbors:

                # Multiple-Path Pruning
                exist = False

                for node in self.visited:
                    if (node == neighbor).all():
                        exist = True
                        break
                
                # If node is not in self.visited
                if exist == False:
                    self.frontier = [path + [neighbor]] + self.frontier
                    self.cost = [cost + distance.euclidean(path[-1], neighbor)] + self.cost

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])