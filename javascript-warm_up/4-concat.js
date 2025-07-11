#!/usr/bin/node

const firstArg = process.argv[2];
const SecondArg = process.argv[3];

if (firstArg !== undefined) {
    console.log(firstArg);
    console.log('is');
}
else {
        console.log('undefined');
        console.log('is');
}
if (SecondArg !== undefined) {
    console.log(SecondArg);
}
else {
        console.log('undefined');
}

