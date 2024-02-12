#!/usr/bin/node

const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  // sort the array
  const SortArgs = args.sort();

  // know the length
  const len = SortArgs.length;

  // search the second biggest integer
  console.log(SortArgs[len - 2]);
}
