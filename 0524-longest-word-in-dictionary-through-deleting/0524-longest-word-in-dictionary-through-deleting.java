class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        Collections.sort(dictionary);
        String ans = "";
        for(String word: dictionary) {
            if(word.length() <= ans.length()) continue;
            int i = 0;
            for(int j = 0; j < s.length(); j++) {
                if(s.charAt(j) == word.charAt(i)) {
                    i += 1;
                    if(i == word.length()) {
                        ans = word;
                        break;
                    }
                }
            }
        }
        return ans;
    }
}