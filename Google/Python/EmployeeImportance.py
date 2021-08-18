"""
You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.
"""


# Helper Class
class Employee:
    def __init__(self, e_id, importance, subordinates):
        self.e_id = e_id
        self.importance = importance
        self.subordinates = subordinates

def setup_problem(list):
    employee_list = []
    for item in list: 
        empl = Employee(item[0],item[1],item[2])
        employee_list.append(empl)
    return employee_list


class Solution:
    def __init__(self):
        self.subs = []

    # Recursively get the subordinates (use the handy dandy class field to do so)
    # eliminates figuring out return statements
    def get_subs(self,e_id,sub_dict):
        self.subs.append(e_id)
        for sub in sub_dict[e_id]:
            self.get_subs(sub,sub_dict)
    def getImportance(self, employees, e_id):
        sub_dict = {}
        val_dict = {}
        for employee in employees:
            sub_dict[employee.e_id] = employee.subordinates
            val_dict[employee.e_id] = employee.importance
        self.get_subs(e_id,sub_dict)
        val = 0
        for employee in self.subs: 
            val+=val_dict[employee]
        return val




if __name__ == "__main__":
    problem_list = [[1,50,[2]],[2,89,[3]],[3,69,[4]],[4,52,[5,26]],[5,78,[6,7]],[6,63,[]],[7,55,[8]],[8,88,[9,25]],[9,64,[10]],[10,54,[11,19]],[11,81,[12]],[12,83,[13,18]],[13,58,[14,15]],[14,64,[]],[15,97,[16]],[16,67,[17]],[17,56,[]],[18,64,[]],[19,95,[20,23]],[20,70,[21,22]],[21,74,[]],[22,95,[]],[23,56,[24]],[24,100,[]],[25,69,[]],[26,98,[]]]
    empl_id = 9
    leet_input = setup_problem(problem_list)
    print(Solution().getImportance(leet_input,empl_id))