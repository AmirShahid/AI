import java.io.FileReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;


public class Sudoko {

    public static class Knowledgebase {
        ArrayList<Integer>[][] hornClause = new ArrayList[4][4];
        int[][] Table;

        public Knowledgebase(int[][] Table) {
            this.Table = Table;
        }

        public boolean notInCol(int x, int col) {
            for (int i = 0; i < 4; i++) {
                if (x == Table[i][col]) {
                    return false;
                }
            }
            return true;
        }

        public boolean notInRow(int x, int row) {
            for (int i = 0; i < 4; i++) {
                if (x == Table[row][i]) {
                    return false;
                }
            }
            return true;
        }

        public boolean notInBlock(int x, int row, int col) {
            int rStart = 0;
            int cStart = 0;
            if (row > 1) {
                rStart = 2;
            }
            if (col > 1) {
                cStart = 2;
            }

            for (int i = rStart; i < rStart + 2; i++) {
                for (int j = cStart; j < cStart + 2; j++) {
                    if (x == Table[i][j]) {
                        return false;
                    }
                }
            }
            return true;
        }

        public void createKnowlageBase() {


            for (int i = 0; i < 4; i++) {

                for (int j = 0; j < 4; j++) {
                    if (Table[i][j] == 0) {

                        ArrayList<Integer> possibleNums = new ArrayList<>();
                        for (int k = 1; k <= 4; k++) {
//                        if (notInRow(k, i)) {
//                            System.out.println(i + " " + j + " not in row : " + k);
//                        }
//                        if (notInCol(k, j)) {
//                            System.out.println(i + " " + j + " not in col : " + k);
//                        }
//                        if (notInBlock(k, i, j)) {
//                            System.out.println(i + " " + j + " not in blk : " + k);
//                        }
//
//
                            if (notInRow(k, i) && notInCol(k, j) && notInBlock(k, i, j)) {
                                possibleNums.add(k);
                            }
                        }
                        hornClause[i][j] = (ArrayList) possibleNums.clone();
                    }

                }
            }
        }

        public void updateKnowledgeBase(int[][] table) {
            Table = table;
            createKnowlageBase();
        }

    }

    int[][] Table = new int[4][4];

    void inserttable() {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                Table[i][j] = scanner.nextInt();

            }
        }
    }

    void printtable() {
        for (int i = 0; i < 4; i++) {
            System.out.println();
            for (int j = 0; j < 4; j++) {
                System.out.print(Table[i][j] + " ");
            }
        }
    }


    public boolean isSolved() {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (Table[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }


    public static void main(String[] args) {
        Sudoko sudoko = new Sudoko();
        System.out.println("Insert Table");
        sudoko.inserttable();
        Knowledgebase kb = new Knowledgebase(sudoko.Table);
        kb.createKnowlageBase();
        while (!sudoko.isSolved()) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (sudoko.Table[i][j] == 0) {
                        if (kb.hornClause[i][j].size() == 1) {
                            sudoko.Table[i][j] = kb.hornClause[i][j].get(0);
                            sudoko.printtable();
                            System.out.println();
                        }
                    }
                }
            }
            kb.updateKnowledgeBase(sudoko.Table);
//            sudoko.printtable();
//            System.out.println();
//            for (int k = 0; k < 4; k++) {
//                for (int l = 0; l < 4; l++) {
//                    if (kb.hornClause[k][l] instanceof ArrayList)
//                        for (int m = 0; m < kb.hornClause[k][l].size(); m++) {
//                            System.out.println(k + " " + l + " : " + kb.hornClause[k][l].get(m));
//                        }
//                }
//            }
        }
        sudoko.printtable();

    }

}