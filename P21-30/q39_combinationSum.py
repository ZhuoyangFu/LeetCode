# can = [2,3,6,7]
# target = 7
# choice = [i for i in can if i<=target]
# print(choice)

# can = [2,3,6,7]
# can.pop()
# print(can)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(path,rem):
            re=[]
            if rem==0:
                temp = tuple(path)
                return [list(temp)]
            choice=[i for i in candidates if i<=rem]
            if len(choice)==0:
                return []
            for i in range(len(choice)):
                path.append(choice[i])
                re.extend(dfs(path,rem-choice[i]))
                path.pop()
            return re

        re1=dfs([],target)
        for j in re1 :
            j.sort()
        return list(set( [tuple(i) for i in re1]))