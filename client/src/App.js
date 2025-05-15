import React, { useState, useEffect } from "react";
import MovieList from "./components/MovieList";
import SearchBar from "./components/SearchBar";
import { sortByKey } from "./utils/sort";
import "./styles/App.css";

const App = () => {
  const [allMovies, setAllMovies] = useState([]);
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const moviesPerPage = 12;

  useEffect(() => {
    setLoading(true);
    const fetchMovies = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/movies");
        const data = await response.json();
        const sorted = sortByKey(data, "title");
        setAllMovies(sorted);
        setMovies(sorted);
      } catch (error) {
        console.error("Error while getting the movies:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchMovies();
  }, []);

  const handleSearch = (query) => {
    setSearchQuery(query);
    const filtered = allMovies.filter((movie) =>
      movie.title.toLowerCase().includes(query.toLowerCase())
    );
    setMovies(sortByKey(filtered, "title"));
    setCurrentPage(1);
  };

  return (
    <div className="app-container">
      <h1>🎬 Movie Searcher</h1>
      <SearchBar searchQuery={searchQuery} handleSearch={handleSearch} />
      {loading ? (
        <p>Loading...</p>
      ) : (
        movies && (
          <MovieList
            movies={movies}
            currentPage={currentPage}
            moviesPerPage={moviesPerPage}
          />
        )
      )}
      <div className="pagination-container">
        <button
          onClick={() => setCurrentPage(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <button
          onClick={() => setCurrentPage(currentPage + 1)}
          disabled={currentPage * moviesPerPage >= movies.length}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default App;
