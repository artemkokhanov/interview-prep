// Design a solution for the following task:
// There is a string s. We need to perform K alternating steps. In the first step, we replace the leftmost letter with
// its corresponding digit ('a' → 1, 'b' → 2, 'c' → 3, ...). In the second step, we replace the rightmost letter.
// This pattern continues with the third step replacing the leftmost letter again, and so on.
// Create code for a function solution that given a string s and an integer K, returns the string after performing
// K steps.

class Solution {
    public String solution(String S, int K) {
        StringBuilder sb = new StringBuilder(S);

        int left = 0;
        int right = sb.length() - 1;

        for (int step = 1; step <= K; step++) {
            if (left > right) {
                break;
            }

            if (step % 2 == 1) {
                while (left <= right && !Character.isLetter(sb.charAt(left))) {
                    left++;
                }
                if (left > right) {
                    break;
                }

                char c = sb.charAt(left);
                int num = (c - 'a') + 1;
                sb.replace(left, left + 1, String.valueOf(num));
                left++;
            } else {
                while (right >= left && !Character.isLetter(sb.charAt(right))) {
                    right--;
                }
                if (right < left) {
                    break;
                }

                char c = sb.charAt(right);
                int num = (c - 'a') + 1;
                sb.replace(right, right + 1, String.valueOf(num));
                right--;
            }
        }

        return sb.toString();
    }
}
