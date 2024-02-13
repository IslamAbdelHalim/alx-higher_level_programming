#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (num) {
    if (base === 16) {
      return num.toString(16).toUpperCase();
    } else {
      return num;
    }
  }

  return myConverter;
};
