"use strict"
var request = require('request');

module.exports = (context, callback) => {
    var url = "http://api.openweathermap.org/data/2.5/weather?q="+context+"&appid=2299edbf49e2c97b3b3a7f7e78669fb7";
    request(url, function (error, response, body) {
        var jsonbody = JSON.parse(body);
        var weather = jsonbody.weather[0].main;
        // console.log(weather);
        // var json = {};
        // json.status="ok";
        // json.err=error;
        // json.res=response;
        // json.body=body;
        callback(undefined, weather);
    });
}
