#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    const char = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }

  print () {
    super.print();
  }
}

module.exports = Square;
