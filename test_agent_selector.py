import unittest
from agent import Agent
from issue import Issue
from agent_selector import AgentSelector
from datetime import time

class TestAgentSelector(unittest.TestCase):

    #this function gets called before every test
    #here we generate data for testing
    def setUp(self):

        #creating agents for testing
        self.agent1 = Agent('kanishk', True, time(9,20,0), ['web developer','analyst'])
        self.agent2 = Agent('ayushya', True, time(8,20,0),['developer','analyst'])
        self.agent3 = Agent('shivi', True, time(1,13,0),['writer', 'support'])
        self.agent4 = Agent('prateek', True, time(14,33,0),['support','sales'])
        self.agent5 = Agent('alex', True, time(6,29,0),['marketing','analyst','support'])
        self.agent6 = Agent('shreya', True, time(2,0,0),['mobile developer','analyst'])
        self.agent7 = Agent('sonam', True, time(0,24,0),['frontend developer', 'support', 'backend developer'])
        self.agent8 = Agent('priya', False, time(3,59,0),['backend develper','ml engineer'])
        self.agent9 = Agent('bablu', True, time(19,44,0),['frontend developer','cloud computing'])

        #list of agents
        self.agent_list = [self.agent1, self.agent2, self.agent3, self.agent4, self.agent5, self.agent6, self.agent7, self.agent8, self.agent9]

        #creating issues for testing
        self.issue1 = Issue(roles= ['support'])
        self.issue2 = Issue(roles = ['marketing'])
        self.issue3 = Issue(roles= ['frontend developer', 'backend developer'])
        self.issue4 = Issue(roles = ['cloud computing'])
        self.issue5 = Issue(roles= ['ml engineer'])
        self.issue6 = Issue(roles = ['writer','support'])
        self.issue7 = Issue(roles = ['cloud architect', 'deeplearning'])
        
        #list of issues
        self.issue_list = [self.issue1, self.issue2, self.issue3, self.issue4, self.issue5, self.issue6, self.issue7]

        #creating agent_ selector ojects
        self.agent_selector1 = AgentSelector('all_available', self.agent_list, self.issue_list)
        self.agent_selector2 = AgentSelector('least_busy', self.agent_list, self.issue_list)
        self.agent_selector3 = AgentSelector('random', self.agent_list, self.issue_list)
        

    #testing match roles function
    def test_match_roles(self):

        self.assertEqual(self.agent_selector1.match_roles(self.agent1.roles,self.issue1.roles),False)
        self.assertEqual(self.agent_selector1.match_roles(self.agent3.roles,self.issue1.roles),True)

    
    #testing select_all_available function
    def test_select_all_available(self):
        
        self.assertCountEqual(self.agent_selector1.select_all_available(self.issue1),[self.agent3,self.agent4,self.agent5,self.agent7])
        self.assertCountEqual(self.agent_selector1.select_all_available(self.issue3),[self.agent7])
        self.assertCountEqual(self.agent_selector1.select_all_available(self.issue7),[])


    #testing select_least_busy function
    def test_select_least_busy(self):
        
        self.assertCountEqual(self.agent_selector2.select_least_busy(self.issue1),[self.agent7])
        self.assertCountEqual(self.agent_selector2.select_least_busy(self.issue4),[self.agent9])
        self.assertCountEqual(self.agent_selector2.select_least_busy(self.issue7),[])
        

    #testing select_agents function
    def test_select_agents(self):

        self.assertCountEqual(self.agent_selector1.select_agents(),[[self.agent7,self.agent3,self.agent5,self.agent4],[self.agent5],[self.agent7],[self.agent9], [],[self.agent3],[]])
        self.assertCountEqual(self.agent_selector2.select_agents(),[[self.agent7],[self.agent5],[self.agent7],[self.agent9], [],[self.agent3],[]])

if __name__ == '__main__':

    unittest.main()






