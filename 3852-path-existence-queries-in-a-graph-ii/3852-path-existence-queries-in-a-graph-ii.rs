impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut pairs: Vec<(i32, usize)> = nums.into_iter().enumerate().map(|(i, x)| (x, i)).collect();
        pairs.sort_unstable_by_key(|k| k.0);

        let mut orig_to_sorted = vec![0; n];
        for i in 0..n {
            orig_to_sorted[pairs[i].1] = i;
        }

        let k_max = 18;
        let mut left_bound = vec![vec![0; n]; k_max];
        let mut right_bound = vec![vec![0; n]; k_max];

        let vals: Vec<i32> = pairs.iter().map(|p| p.0).collect();

        for i in 0..n {
            let val = vals[i];
            let l_val = val - max_diff;
            let r_val = val + max_diff;

            left_bound[0][i] = vals.partition_point(|&x| x < l_val);
            right_bound[0][i] = vals.partition_point(|&x| x <= r_val) - 1;
        }

        for k in 1..k_max {
            for i in 0..n {
                left_bound[k][i] = left_bound[k - 1][left_bound[k - 1][i]];
                right_bound[k][i] = right_bound[k - 1][right_bound[k - 1][i]];
            }
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let u = q[0] as usize;
            let v = q[1] as usize;
            if u == v {
                ans.push(0);
                continue;
            }

            let su = orig_to_sorted[u];
            let sv = orig_to_sorted[v];

            let mut curr_l = su;
            let mut curr_r = su;

            if sv < left_bound[k_max - 1][curr_l] || sv > right_bound[k_max - 1][curr_r] {
                ans.push(-1);
                continue;
            }

            let mut steps = 0;
            for k in (0..k_max).rev() {
                let next_l = left_bound[k][curr_l];
                let next_r = right_bound[k][curr_r];

                if sv < next_l || sv > next_r {
                    curr_l = next_l;
                    curr_r = next_r;
                    steps += 1 << k;
                }
            }
            ans.push(steps + 1);
        }

        ans
    }
}