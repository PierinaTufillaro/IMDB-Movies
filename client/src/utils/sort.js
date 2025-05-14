export const sortByKey = (array, key) => {
  return [...array].sort((a, b) => {
    const textA = a[key].toLowerCase();
    const textB = b[key].toLowerCase();
    return textA.localeCompare(textB);
  });
};
