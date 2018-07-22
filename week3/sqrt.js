const sqrt = (n, maxDiff) => {
  let acc = 0
  let guess = 1
  while (!isValid(guess, Math.sqrt(n), maxDiff)) {
    acc += 1
    guess = (guess + n / guess) / 2
  }
  console.log(acc, guess)
  return guess
}

const isValid = (guess, correct, maxDiff) => {
  return Math.abs(guess - correct) <= maxDiff
}

const getSqrt = (n) => {
  let acc = 0
  let sqrt = 0.01
  while (sqrt * sqrt <= n) {
    acc += 1
    sqrt = parseFloat((sqrt + 0.01).toFixed(2))
  }
  console.log(acc)
  if (sqrt * sqrt > n) sqrt = parseFloat((sqrt - 0.01).toFixed(2))
  return sqrt
}

sqrt(144, 0.001)
getSqrt(144)
