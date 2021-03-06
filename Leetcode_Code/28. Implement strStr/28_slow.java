public class Solution {
    public static int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (haystack.length() >= needle.length())
            for (int i = 0; i < haystack.length() - needle.length() + 1; ++i) {
                for (int j = 0; j < needle.length(); ++j) {
                    if (haystack.charAt(i + j) != needle.charAt(j)) {
                        break;
                    } else if (j == needle.length() - 1) return i;
                }
            }
        return -1;
    }
}
