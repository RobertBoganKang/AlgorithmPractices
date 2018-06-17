class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = {'a', 'e', 'i', 'o', 'u',
                 'A', 'E', 'I', 'O', 'U'}
        S = S.strip()
        S += ' '
        i = 0
        string_builder = ""
        word_count = 1
        while i < len(S):
            j = 0
            first_letter = ""
            while i < len(S) and S[i] != ' ':
                if j == 0 and S[i] not in vowel:
                    first_letter = S[i]
                else:
                    string_builder += S[i]
                j += 1
                i += 1
            string_builder += first_letter
            string_builder += 'ma'
            for _ in range(word_count):
                string_builder += 'a'
            string_builder += ' '
            word_count += 1
            i += 1
        return string_builder[:len(string_builder) - 1]
