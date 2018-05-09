"use strict"

var request = require('request');
var openfaas = "https://maker.ifttt.com/trigger/openfaas/with/key/diGWR1we397BBxqRdvMS3X";

module.exports = (context, callback) => {
    request.post({url:openfaas, form: {value1:context}}, function (error, response, body) {
        if (error) {
            callback(error, {status: "error"});
            return;
        }
        callback(undefined, {status: "done"});
    })

}
