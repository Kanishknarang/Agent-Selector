#importing modules
from agent import Agent
from issue import Issue
from datetime import time
import random

#class for creating agent selector
class AgentSelector:


    #constructor
    #here we initialize the agent_selection_mode, list of all the agents and the queue of issues to be assigned to agents
    def __init__(self, agent_selection_mode, agent_list, issues_queue):

        self.agent_selection_mode = agent_selection_mode
        self.agent_list = agent_list
        self.agent_list.sort(key=lambda x: x.available_since) #sorting agent list on the basis of available_since attribute
        self.issues_queue = issues_queue


    
    def match_roles(self, agent_roles, issue_roles):

        '''This function compares the roles of the issue and agent.if all the roles in issue are also there in agent,
        it returns true else false'''
        
        for issue_role in issue_roles:
            
            if issue_role not in agent_roles:
                return False
        
        return True       

    
    def select_all_available(self, issue):

        '''This function is called when the agent_selection_mode is all_available
        It iterates through all the agents and checks if the agent is available and if the roles of agent matches with that
        of issue.If so it gets added to a list.After all the agents are found the list is returned'''

        #this list stores all the found agents
        selected_agents = []

        for agent in self.agent_list:
            
            if agent.is_available and self.match_roles( agent.roles, issue.roles):
                selected_agents.append(agent)
        
        return selected_agents
                    

    def select_least_busy(self, issue):

        '''This function is called when agent_selection_mode is least_busy.
        As we have alredy sorted the agents list based on the available since attribute.
        The first agent that matches the roles of the issue will be least busy.
        Therefore it traverses through all the agents and returns the first agent whose roles match with the issue  
        '''

        #this list stores all the found agents
        selected_agents = []

        for agent in self.agent_list:
            
            if agent.is_available and self.match_roles( agent.roles, issue.roles):
                selected_agents.append(agent)                
                break
        
        return selected_agents

    
    def select_random(self, issue):

        '''This function is called when the agent_selection_mode is random.
        It first adds all the agents that match the roles of the issue to a list.
        This it generates a random integer between 0 and length of list-1 using random module.
        Then returns the agent at that index'''

        #this list stores all the found agents
        selected_agents = []

        for agent in self.agent_list:
            
            if agent.is_available and self.match_roles( agent.roles, issue.roles):
                selected_agents.append(agent)


        l = len(selected_agents)  

        #generating random integer between 0 and l-1
        i = random.randint(0,l-1)

        # adding agent at that random index to list
        selected_agents = [selected_agents[i]]       
        
        return selected_agents
    
    def select_agents(self):

        '''This function is used for selecting agents for all the issues.
        It goes through all the issues and for each issue it find the agents based on the agent_selection_mode'''

        #This variable will refer to a list of lists, where each inner list will contain the the agents for one particular issue.
        selected_agents_for_all_issues = []
        
        for issue in self.issues_queue:

            if self.agent_selection_mode == 'all_available':

                #this variable refers to a list which contains selected agents for one issue 
                selected_agents_per_issue = self.select_all_available(issue)

            elif self.agent_selection_mode == 'least_busy':

                #this variable refers to a list which contains selected agents for one issue 
                selected_agents_per_issue = self.select_least_busy(issue)

            else:

                #this variable refers to a list which contains selected agents for one issue 
                selected_agents_per_issue = self.select_random(issue)

            selected_agents_for_all_issues.append(selected_agents_per_issue)

        return selected_agents_for_all_issues


if __name__ == '__main__':
    agent1 = Agent('kanishk', True, time(9,20,0),['developer','analyst'])
    agent2 = Agent('ayushya', True, time(8,20,0),['developer','analyst', 'writer'])

    agent_list = [agent1,agent2]

    issue1 = Issue(roles= ['developer','analyst'])
    issue2 = Issue(roles = ['analyst'])

    issue_list = [issue1, issue2]

    agent_selector = AgentSelector('random', agent_list, issue_list)
    print(agent_selector.select_agents())

    for selected_agents in agent_selector.select_agents():
        for selected_agents_per_issue in selected_agents:
            print(selected_agents_per_issue)
        print()