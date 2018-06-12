"use strict"

module.exports = (context, callback) => {
    var regression = require("regression");
    var j = JSON.parse(context);
    let vectors = new Array();
    // var X_train = j["X_train"];
    // for (let i = 0 ; i < X_train.length ; i++) {
    //   vectors[i] = X_train[i]["vector"]
    // }
    const result = regression.linear([[1,1], [2,1], [0,0], [1,1]]);
    const gradient = result.equation[0];
    const yIntercept = result.equation[1];
    callback(undefined, gradient);
    callback(undefined, yIntercept);
    callback(undefined, regression.predict(1));
    // var y_test = j["y_test"];
    // for (let i = 0 ; i < y_test.length ; i++) {
    //     // yvectors[i] = y_train[i]["vector"]
        // callback(undefined, regression.predict(y_test[i]))
    // }

}
