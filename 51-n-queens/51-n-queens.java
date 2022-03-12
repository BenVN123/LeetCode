class Solution {
    public List <List <String>> res;
    
    public List <List <String>> solveNQueens (int n) {        
        String board [][] = new String [n][n];
        res = new ArrayList ();
        for (String row [] : board)
            Arrays.fill (row, ".");
        Solve (board, 0);
        return res;
    }
    
    public void addToResult (String board [][]) {
        List <String> list = new ArrayList ();
        for (int i = 0; i < board.length; i++) {
            String str = "";
            for (int j = 0; j < board.length; j++)
                str += board [i][j];
            list.add (str);
        }
        res.add (list);
    }
    
    public void Solve (String board [][], int row) {
        if (row >= board.length) {
            addToResult (board);
            return;
        }
        for (int i = 0; i < board.length; i++) {
            if (isSafe (board, row, i)) {
                board [row][i] = "Q";
                Solve (board, row + 1);
                board [row][i] = ".";
            }
        }
    }
    
    public boolean isSafe (String board [][], int row, int col) {
        for (int i = 0; i < board.length; i++) {
            if (board [i][col].equals ("Q") && i != row)
                return false;
        }
		
        int i = row - 1;
        int j = col - 1;
        while (i >= 0 && j >= 0) {
            if (board [i][j].equals("Q"))
                return false;
            i--;
            j--;
        }
		
        i = row + 1;
        j = col + 1;
        while (i < board.length && j < board[0].length) {
            if (board [i][j].equals("Q"))
                return false;
            i++;
            j++;
        }
		
        i = row + 1;
        j = col - 1;
        while (i < board.length && j >= 0) {
            if (board [i][j].equals("Q"))
                return false;
            i++;
            j--;
        }
		
        i = row - 1;
        j = col + 1;
        while (i >= 0 && j < board[0].length) {
            if (board [i][j].equals("Q"))
                return false;
            i--;
            j++;
        }
        return true;
    }
}