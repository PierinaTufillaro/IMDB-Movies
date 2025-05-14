import React from "react";

const SearchBar = ({ searchQuery, handleSearch }) => {
  return (
    <div>
      <input
        type="text"
        placeholder="Search by title."
        value={searchQuery}
        onChange={(e) => handleSearch(e.target.value)}
      />
    </div>
  );
};

export default SearchBar;
