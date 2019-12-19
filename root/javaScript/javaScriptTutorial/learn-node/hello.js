/**
 * hello.js
 * */
module.exports = {
    anything : function() {
        console.log('I am anything.');
    },
}

// ALERT - this won't be exported.
exports.bye = function() {
    console.log('bye');
};
