// Task(0): Edit these given functions
/*export function taskFirst() {
var task = 'I prefer const when I can.';
return task;
}

export function getLast() {
return ' is okay';
}

export function taskNext() {
var combination = 'But sometimes let';
combination += getLast();

return combination;
}*/

const babel = require("@babel/core");

babel.transformSync("code", optionsObject);

export function taskFirst() {
var task = 'I prefer const when I can.';
return task;
}

export function getLast() {
return ' is okay';
}

export function taskNext() {
var combination = 'But sometimes let';
combination += getLast();

return combination;
}
