from knowledge_base import *

class LogicalAgent():

    def __init__(self,KB):
        self.KB = KB

    # TODO
    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB

        Returns:
            A list with all the logical consequences of KB
        '''
        C = []

        for ask in self.KB.askables:
            if ask not in C:
                x = True if input(f'atom {ask.atom} is true (y or n)? ') == 'y' else False

                if x:
                    C.append(ask.atom)

        while True:
            select = False
            for clause in self.KB.clauses:
                if clause.head not in C and (all(map(lambda x: x in C, clause.body))):
                    C.append(clause.head)
                    select = True
            if select == False:
                break
        return C

    # TODO
    def top_down(self,query):
        '''Implements the top down proof strategy. Given a query (the atom that it wants to prove) 
        it returns True if the query is a consequence of the knowledge base. 
        
        Args:
            querry: The atom that should be proved

        Returns: 
            True if the query is a logical consequence of KB, False otherwise

        '''
        G = query
        
        while G != []:
            findClause = False

            for statement in self.KB.statements:
                if isinstance(statement, Clause):
                    if statement.head == G[0]:
                        G.pop(0)
                        G = statement.body + G
                        findClause = True
                        break

                if isinstance(statement, Askable):
                    if statement.atom == G[0]:
                        x = True if input(f'atom {statement.atom} is true (y or n)? ') == 'y' else False
                        if x:
                            G.pop(0)
                            findClause = True
                            break
                            
                
            if findClause == False:
                return False

        return True
    
    # TODO
    def explain(self,g):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.

        Args:
            g: A set of atoms that should be explained
        
        Returns:
            A list of explanation for the atoms in g
        '''

        '''
        C = []

        for statement in self.KB.statements:
            if isinstance(statement, Assumable):
                C.append((statement.atom, [statement.atom]))

        for clause in self.KB.clauses:
            #print([c for x in clause.body for c in C if x == c[0]].__len__() == clause.body.__len__())
            if all(map(lambda x: (x, ...) in C, clause.body)):
                C.append((clause.head, [x[1] for x in C if x[0] in clause.body]))
                                        
            print(list(map(lambda x: (x, ) in C, clause.body)))
        
        print(C)
        '''

        pass