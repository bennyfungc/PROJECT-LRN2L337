class Solution {
  public boolean judgeCircle(String moves) {

    int x = 0;
    int y = 0;

    for(int i = 0; i < moves.length(); i++) {
      // Move coordinate up
      if(moves.charAt(i) == 'U') {
        ++y;
        continue;
      }

      // Move coordinate down
      if(moves.charAt(i) == 'D') {
        --y;
        continue;
      }

      // Move coordinate left
      if(moves.charAt(i) == 'L') {
        --x;
        continue;
      }

      // Move coordinate right
      if(moves.charAt(i) == 'R') {
        ++x;
        continue;
      }
    }

    if((x == 0) && (y == 0)) {
      return true;
    }
    else {
      return false;
    }
  }
}
