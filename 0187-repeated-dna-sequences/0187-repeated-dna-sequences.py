class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # create a window of 10 letters as one substring
        # Compare it against each char as start 
        # first 10 letters are assinged a value hash function
        # then we check this hash func value to the string s windows of 10
        # if hash matches we found a repeated sequecne
        # collision if occured check char by char


        # went in another direction altogether

        # below solution saw it and easy to solve
        seen  =set()
        repeat = set()
        for i in range(len(s) - 9):
            substr = s[i:i+10]
            if substr in seen:
                repeat.add(substr)
            else:
                seen.add(substr)
        return list(repeat)


        