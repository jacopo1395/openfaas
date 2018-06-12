
regression = require("regression");
const result = regression.linear([[1,1], [2,1], [0,0], [1,1]]);
const gradient = result.equation[0];
const yIntercept = result.equation[1];
console.log(result);
console.log(gradient);
console.log(yIntercept);
console.log(result.predict( [1,2,3] ));
