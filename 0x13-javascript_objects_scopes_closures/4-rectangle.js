#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method exchange the width and height
  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  // method multiple the width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
