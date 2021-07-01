# *_* coding : UTF-8 *_*
# Author ： jiangxiaolong
# time   ： 2021/5/13  下午3:09


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 排序
    numbers = sorted(nums)

    resp = []

    for i in range(0, len(numbers)):

        # 最小值大于0 直接break
        if numbers[i] > 0:
            break

        left = i + 1
        right = len(numbers) - 1

        while left < right:

            temp_sum = numbers[left] + numbers[right] + numbers[i]
            # 刚好等于0
            if temp_sum == 0:
                temp_list = sorted([numbers[left], numbers[right], numbers[i]])
                print(temp_list)
                if temp_list not in resp:
                    resp.append([numbers[left], numbers[right], numbers[i]])

                left += 1
                right -= 1

            elif temp_sum > 0:
                # 说明右边的值太大，右指针往前移
                right -= 1

            else:
                # 说明左边的值太小，左指针往后一
                left += 1

    return resp


# nums = [-2, 0, 1, 1, 2]
# three_sum = threeSum(nums)
# print(three_sum)

nums = [1, 1, 1, 1]

for i in nums[:]:
    if nums.count(i) != 1:
        nums.remove(i)

print(nums)
