public class LineSegmentIntersections {

    public static int countIntersections(int[] P, int[] Q) {
        int n = P.length;
        int intersections = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((P[i] < P[j] && Q[i] > Q[j]) || (P[i] > P[j] && Q[i] < Q[j])) {
                    intersections++;
                }
            }
        }
        
        return intersections;
    }

    public static void main(String[] args) {

        int[] P1 = {1, 2, 3};
        int[] Q1 = {3, 2, 1};
        System.out.println("Number of intersections (Example 1): " + countIntersections(P1, Q1)); // output: 3


        int[] P2 = {1, 3, 2};
        int[] Q2 = {1, 2, 3};
        System.out.println("Number of intersections (Example 2): " + countIntersections(P2, Q2)); // output: 1


        int[] P3 = {1, 2, 3};
        int[] Q3 = {1, 2, 3};
        System.out.println("Number of intersections (Example 3): " + countIntersections(P3, Q3)); // output: 0
    }
}