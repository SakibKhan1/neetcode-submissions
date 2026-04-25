class Solution {
    public int hammingWeight(int n) {
        int res = 0;

        for (int i = 0; i < 32; i++) {
            int lastBit = n & 1;

            if (lastBit == 1) {
                res += 1;
            }

            n >>= 1;
        }

        return res;
    }
}
