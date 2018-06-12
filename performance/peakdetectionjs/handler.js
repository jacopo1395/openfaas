"use strict"

module.exports = (context, callback) => {
    var j = JSON.parse(context);
    var slayer = require('slayer');
    var arrayData = j["data"];

    slayer().fromArray(arrayData).then(spikes => {
      // console.log(spikes);      // [ { x: 4, y: 12 }, { x: 12, y: 25 } ]
      callback(undefined, spikes);
    });
}
