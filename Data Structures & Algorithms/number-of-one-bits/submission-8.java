class Solution {
    public int hammingWeight(int n) {
        int counter = 0;

        while (n != 0) {
            int last_bit = n % 2;
            counter += last_bit ^ 0;

            n >>= 1;
        }

        return counter;
    }
}
