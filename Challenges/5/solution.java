/**
 * solution
 * 1315
 */
public class solution {

    public static void lookAndSay(int n) {
        int x = 1;
        String nthTerm = "00";

        System.err.println("START OF X LOOP");
        while ( x <= n) {
            String currentNthTerm = nthTerm;
            nthTerm = "";
            char currentDigit = currentNthTerm.charAt(0);
            int count = 1;
            int i = 1;
            
            while (i <= currentNthTerm.length()) {
                if (x == 1) {
                    nthTerm = "1";
                } else if (i == currentNthTerm.length()) {
                    nthTerm = nthTerm + count + currentDigit;             
                } else {
                    if (currentDigit == currentNthTerm.charAt(i)) {
                        count +=1;
                    } else {
                        nthTerm =  nthTerm + count + currentDigit;
                        currentDigit = currentNthTerm.charAt(i);
                        count = 1;
                    }
                }
                i++;
            }
            System.out.println(x + " " + nthTerm);
            x++;
        }
    }

    public static void main(String[] args) {
        lookAndSay(6);
    }
}