// accepts two arguments integers (a, b), rounds a and b and returns the sum of it

function calculateNumber(a, b) {
  a = Math.round(a);
  b = Math.round(b);
  return (a + b);
}

module.exports = calculateNumber;
