import java.util.*;

class Solution {
    public String findTheString(int[][] lcp) {
        int n = lcp.length;

        // Step 1: Validate diagonal
        for (int i = 0; i < n; i++) {
            if (lcp[i][i] != n - i) return "";
        }

        // Step 2: DSU (Union-Find)
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        // Find
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (lcp[i][j] > 0) {
                    union(parent, i, j);
                }
            }
        }

        // Step 3: Assign characters
        char[] res = new char[n];
        Map<Integer, Character> map = new HashMap<>();
        char ch = 'a';

        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            if (!map.containsKey(root)) {
                if (ch > 'z') return "";
                map.put(root, ch++);
            }
            res[i] = map.get(root);
        }

        // Step 4: Validate LCP
        int[][] computed = new int[n][n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (res[i] == res[j]) {
                    if (i + 1 < n && j + 1 < n)
                        computed[i][j] = 1 + computed[i + 1][j + 1];
                    else
                        computed[i][j] = 1;
                } else {
                    computed[i][j] = 0;
                }

                if (computed[i][j] != lcp[i][j]) {
                    return "";
                }
            }
        }

        return new String(res);
    }

    private int find(int[] parent, int x) {
        if (parent[x] != x)
            parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    private void union(int[] parent, int a, int b) {
        int pa = find(parent, a);
        int pb = find(parent, b);
        if (pa != pb) parent[pa] = pb;
    }
}