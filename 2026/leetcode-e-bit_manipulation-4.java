import java.util.HashMap;


class Solution {
    public static void main (String [] args) {
        String[] inputs = {"abccbaacz", "abcdd"};
        char[] outputs = {'c', 'd'};
        Solution test = new Solution();
        for (int i = 0; i < inputs.length; i++) {
            char result = test.repeatedCharacter(inputs[i]);
            System.out.println(result == outputs[i] ? "ok" : "fail");
        }
    }

    public char repeatedCharacter(String s) {
        char result = '\0';
        HashMap<Character, Integer> cache = new HashMap<>();
        for (int i = 0; i < s.length() ; i++) {
            if (cache.get(s.charAt(i)) == null) {
                cache.put(s.charAt(i), 0);
            }

            cache.put(s.charAt(i), cache.get(s.charAt(i)) + 1);
            if (cache.get(s.charAt(i)) == 2) {
                result = s.charAt(i);
                break;
            }
        }
        return result;
    }

}

// Problem: 2351. First Letter to Appear Twice
// Date: 2026-01-04
// Link: https://leetcode.com/problems/first-letter-to-appear-twice/solutions/7466930/2351_e_java-by-sharrrkkk-4nxr/
// Notes: