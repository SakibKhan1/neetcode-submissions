class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for i in range(len(order)):
            mapping[order[i]] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            boolval = False  # tracks if order was decided

            for j in range(len(min(word1, word2, key=len))):
                if mapping[word1[j]] == mapping[word2[j]]:
                    continue
                elif mapping[word1[j]] < mapping[word2[j]]:
                    boolval = True
                    break
                else:
                    return False

            # prefix case: all chars same but word1 longer
            if not boolval and len(word1) > len(word2):
                return False

        return True
