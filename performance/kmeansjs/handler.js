"use strict"

module.exports = (context, callback) => {
    var j = JSON.parse(context);
    var dataset = j["dataset"]
    let vectors = new Array();
    for (let i = 0 ; i < dataset.length ; i++) {
      vectors[i] = dataset[i]["vector"]
    }

    const kmeans = require('node-kmeans');
    kmeans.clusterize(vectors, {k: j["n_clusters"]}, (err,res) => {
      if (err) console.error(err);
      else
        callback(undefined, res);
    });
}
