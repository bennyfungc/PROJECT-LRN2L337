class Solution {
  public int findComplement(int num) {
    int x = 0;

    while(x < num) {
      x = (x << 1) + 1;
    }

    return x - num;
  }
}
