//Task(3) - Utils module that exports a single function from task (2)
const Utils = {
  calculateNumber: (type, a, b) => {
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
}

module.exports = Utils;
