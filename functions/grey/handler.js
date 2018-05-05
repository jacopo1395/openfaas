"use strict"
const download = require('image-downloader')
var Jimp = require("jimp");
const fs = require('fs');



module.exports = (context, callback) => {
    // Download to a directory and save with the original filename
    const options = {
        url: context,
        dest: './image.jpg'
    }
    download.image(options)
        .then(({
            filename,
            image
        }) => {
            Jimp.read(filename, function(err, img) {
                if (err) {
                    callback(err, {status: "error"});
                    return;
                }
                img.greyscale().write("img.jpg");

                fs.readFile('./img.jpg', (err, data) => {
                    if (err) {
                        callback(err, {status: "error"});
                        return;
                    }
                    callback(undefined, data);
                });
            });

        }).catch((err) => {
            callback(err, {status: "error"});
        })

}
