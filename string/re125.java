package string;

class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        char a, b;

        
        while (i < j) {
            a = Character.toLowerCase(s.charAt(i));
            b = Character.toLowerCase(s.charAt(j));
            if (Character.isLetterOrDigit(a) && Character.isLetterOrDigit(b)) {
                if (a != b) {
                    return false;
                }
                else {
                    i++;
                    j++;
                    continue;
                }
            }
            i += (Character.isLetterOrDigit(a)) ? 0 : 1;
            j += (Character.isLetterOrDigit(b)) ? 0 : 1;
        }
        return true;
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "A man, a plan, a canal: Panama";
        System.out.println(solution.isPalindrome(s));
    }

}


