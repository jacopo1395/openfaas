const download = require('image-downloader')
var Jimp = require("jimp");

const options = {
    url: "http://www.personal.psu.edu/oeo5025/jpg.jpg",
    dest: './image.jpg'
}
download.image(options)
.then(({ filename, image }) => {
    Jimp.read(filename, function(err, img) {
        if (err) throw err;
        img.greyscale() // set greyscale
            .write("img.jpg"); // save
        // callback(undefined, {status: "done"});
        console.log("ok");
    });

}).catch((err) => {
    // callback(err, {status: "error"});
    console.log(err);
})
