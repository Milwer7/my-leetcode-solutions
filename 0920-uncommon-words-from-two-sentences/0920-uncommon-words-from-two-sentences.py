class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        total_words = [*s1.split(), *s2.split()]
        uncommon_list = [word for word in total_words if total_words.count(word) == 1]
        return uncommon_list