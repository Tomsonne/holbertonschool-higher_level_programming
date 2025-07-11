#!/usr/bin/node

const argCount = process.argv.slice(2);

if (argCount.lenght === 0) {
    console.log('No argument');
} else if (argCount.lenght === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
