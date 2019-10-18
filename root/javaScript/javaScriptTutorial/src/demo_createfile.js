// Create Files
var fs = require('fs');

/**
 * fs.appendFile() : appends specified content to a file. If the file does not exist, the file will be created.
 * */
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved');
});


/**
 * fs.open() : takes a "flag" as the second argument,
 *      w: writing
 *      r: reading
 *      a: appending
 * */
fs.open('mynewfile2.txt', 'w', function (err, file) {
    if (err) throw err;
    console.log('Saved!');
});

/**
 * fs.writeFile() : replaced the specified file and content if it exists. If the file does not exist, a new file, containing the specified content, will be created.
 * */
fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved!');
});

/**
 * Update Files
 *      fs.appendFile()
 *      fs.writeFile()
 * */
fs.writeFile('mynewfile3.txt', 'This is my text', function (err) {
    if (err) throw err;
    console.log('Replaced!');
});

/**
 * Delete Files
 *  fs.unlink() : to delete a file with the File System module
 * */
fs.unlink('mynewfile2.txt', function (err) {
    if (err) throw err;
    console.log('File deleted!');
});
