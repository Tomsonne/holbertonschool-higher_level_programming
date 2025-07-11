#!/usr/bin/node

const firstArg = process.argv[2];
const SecondArg = process.argv[3];

if (firstArg !== undefined) {
    process.stdout.write(firstArg);
    process.stdout.write('is');
}
else {
        process.stdout.write('undefined');
        cprocess.stdout.write('is');
}
if (SecondArg !== undefined) {
    process.stdout.write(SecondArg);
}
else {
        process.stdout.write('undefined');
}

