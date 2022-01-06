// accepts two arguments integers (a, b), rounds a and b and returns the sum of it

function calculateNumber(type, a, b) {
  a = Math.round(a);
  b = Math.round(b);
  if (type === 'SUM') {
    return (a + b); 
  }
  if (type === 'SUBTRACT') {
    return (a - b); 
  }
  if (type === 'DIVIDE') {
    if (b === 0) {
      return ('Error');
    }
    return (a / b);
  }

}

module.exports = calculateNumber;
