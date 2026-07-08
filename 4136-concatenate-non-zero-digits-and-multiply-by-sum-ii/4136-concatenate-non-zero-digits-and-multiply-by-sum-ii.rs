impl Solution {
    pub fn sum_and_multiply(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut nz_digits = Vec::new();
        let mut nz_indices = Vec::new();
        for (i, ch) in s.chars().enumerate() {
            if ch != '0' {
                nz_digits.push((ch as u8 - b'0') as i64);
                nz_indices.push(i as i32);
            }
        }
        
        let n = nz_digits.len();
        let mut pref_sum = vec![0i64; n + 1];
        let mut pref_val = vec![0i64; n + 1];
        let m_mod = 1_000_000_007i64;
        
        for i in 0..n {
            pref_sum[i + 1] = pref_sum[i] + nz_digits[i];
            pref_val[i + 1] = (pref_val[i] * 10 + nz_digits[i]) % m_mod;
        }
        
        let mut pow10 = vec![1i64; n + 1];
        for i in 1..=n {
            pow10[i] = (pow10[i - 1] * 10) % m_mod;
        }
        
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let l = q[0];
            let r = q[1];
            
            let start_idx = nz_indices.partition_point(|&x| x < l);
            let end_idx = nz_indices.partition_point(|&x| x <= r);
            
            if start_idx >= end_idx {
                ans.push(0);
            } else {
                let count = end_idx - start_idx;
                let sum = pref_sum[end_idx] - pref_sum[start_idx];
                
                let mut x = (pref_val[end_idx] - (pref_val[start_idx] * pow10[count]) % m_mod) % m_mod;
                if x < 0 {
                    x += m_mod;
                }
                
                let res = (x * (sum % m_mod)) % m_mod;
                ans.push(res as i32);
            }
        }
        ans
    }
}