public class Solution {
    private int TriangleNumber(int n) {
        int trial_number = 0, count, sum;
        boolean test = true;
        while (test) {
            trial_number++;
            count = 0;
            sum = 0;
            for (int trial_divisor = 1; trial_divisor < trial_number; trial_divisor++) {
                if (trial_number % trial_divisor == 0) {
                    sum += trial_divisor;
                    count++;
                }
            }
            if (sum == trial_number && count >= n - 1) {
                test = false;
            }
        }
        return trial_number;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.TriangleNumber(5));
    }
}
