class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var cache: [Int: Int] = [:]
        for (i, num) in nums.enumerated() {
            let comp = target - num
            if let value = cache[comp] {
                return [value, i]
            }
            cache[num] = i
        }
        return [-1]
    }
}
