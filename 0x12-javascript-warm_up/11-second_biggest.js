#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  // sort the array
  const SortArgs = args.map(Number).slice(2).sort((a, b) => a - b);

  // know the length
  const len = SortArgs.length;

  // search the second biggest integer
  console.log(SortArgs[len - 2]);
}
