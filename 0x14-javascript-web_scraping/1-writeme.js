#!/usr/bin/node
const fs = require('fs');
const [filePath, contentToWrite] = process.argv.slice(2);
if (!filePath || !contentToWrite) {
  console.error('Please provide both the file path and content as arguments.');
  process.exit(1);
}
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
