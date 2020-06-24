# Agent-Selector

The project consists of 4 files:
-agent.py : consists of a class Agent used for creating agent objects
-issue.py : consists of a class Issue used for creating issue objects
-agent_selector.py : it is the main file of the project where all the work of selecting agents is done.
-test_agent_selector : it consists of unit tests for testing our project


agent.py->

this file consists of a class Agent which is used for creating Agent objects.
The agent field are : name, is_available, available_since roles(list of roles)

issues.py->

this file consists of a class Issue which is used for creating Issue objects.
The agent field are : discription, roles(list of roles)

agent_selector.py->

agent_selector.py file consists of a class AgentSelector.This class creates has 3 attributes
1- agent_selection_mode
2- agent_list : we sort the agent list on the basis of available since attribute.This helps in finding the least_busy agent.
3- issues_queue

AgentSelector class has following functions:

1- match_roles() - This function compares the roles of the issue and agent.if all the roles in issue are also there in agent,it returns true else false.

2- select_all_available - This function is called when the agent_selection_mode is all_available.It iterates through all the agents and checks if the agent is available and if the roles of agent matches with that of issue.If so it gets added to a list.After all the agents are found the list is returned.

3- select_least_busy - This function is called when agent_selection_mode is least_busy.As we have alredy sorted the agents list based on the available since attribute.The first agent that matches the roles of the issue will be least busy.Therefore it traverses through all the agents and returns the first agent whose roles match with the issue

4- select_random - This function is called when the agent_selection_mode is random.It first adds all the agents that match the roles of the issue to a list.Then it generates a random integer between 0 and (length of list-1) using random module.Then returns the agent at that index.

5- select_agents - This function is used for selecting agents for all the issues.It goes through all the issues and for each issue it find the agents based on the agent_selection_mode

test_agent_selector.py->

This file consists of unittests for testing our project.
