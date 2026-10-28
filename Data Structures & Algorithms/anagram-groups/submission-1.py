class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        #strs = ["act","pots","tops","cat","stop","hat"]
        arr =[]
        i = 0
        while(i<len(strs)):
            arr.append("".join(sorted(strs[i])))
            i+=1
        #print(strs)
        #print(arr)

        #dictionary
        a =list( set(arr))
        #print(a)
        dict ={
        
        }
        for key in a:
            dict[key]=[]
            for i in range(0, len(strs)):
                if(key == arr[i]):
                    dict[key].append(strs[i])
        return list(dict.values())
        """
        dict ={}
        
        for word in strs:
            key = "".join(sorted(word))
            if key not in dict:
                dict[key] = []
            dict[key].append(word)
    
        return list(dict.values())