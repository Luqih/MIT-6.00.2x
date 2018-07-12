# generate all combinations of N items
def ternary (n, size):
  if n == 0:
    end = '0'
    while (len(end) < size):
      end = '0' + end
    return end
  nums = []
  while n:
    n, r = divmod(n, 3)
    nums.append(str(r))
  end = ''.join(reversed(nums))
  while (len(end) < size):
    end = '0' + end
  return end

def yieldAllCombos (items):
  N = len(items)
  for i in range(3**N):
    combo = ([], [])
    tern = ternary(i, N)
    for j in range(N):
      if (tern[j] == '1'):
        combo[0].append(items[j])
      if (tern[j] == '2'):
        combo[1].append(items[j])
    yield combo

yieldAllCombos([1,2,3])
