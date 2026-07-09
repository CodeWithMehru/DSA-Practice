impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n_usize = n as usize;
        let mut comp = vec![0; n_usize];
        
        for i in 1..n_usize {
            if nums[i] - nums[i - 1] <= max_diff {
                comp[i] = comp[i - 1];
            } else {
                comp[i] = comp[i - 1] + 1;
            }
        }
        
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let u = q[0] as usize;
            let v = q[1] as usize;
            ans.push(comp[u] == comp[v]);
        }
        
        ans
    }
}