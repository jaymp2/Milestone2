#assemble_genome

def assemble_genome(dna_list):
  n = len(dna_list)
  overlaps = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      x, y = dna_list[i], dna_list[j]
      size = len(x)
      for k in range(1, size):
        if y.startswith(x[k:]):
          overlaps[i][j] = size - k
          break

  def new(i, mask):
    if mask == (1<<n) - 1:
      return dna_list[i]
    ans = '#' * 320
    for j in range(n):
      if mask & (1<<j) == 0:
        k = overlaps[i][j]
        string = new(j, mask | (1<<j))
        if len(dna_list[i] + string[k:]) < len(ans):
          ans = dna_list[i] + string[k:]
    return ans
  return min([new(i, 1<<i) for i in range(n)], key=len)

