import React from 'react';

const MovieList = ({ movies, currentPage, moviesPerPage }) => {
  const indexOfLastMovie = currentPage * moviesPerPage;
  const indexOfFirstMovie = indexOfLastMovie - moviesPerPage;
  const currentMovies = movies.slice(indexOfFirstMovie, indexOfLastMovie);

  return (
    <div className="movie-list-container">
      {currentMovies.length > 0 ? (
        currentMovies.map((movie) => (
          <div key={movie.id} className="movie-card">
            <h3>{movie.title}</h3>
            <p><strong>IMDb Title Id:</strong> {movie.imdb_title_id}</p>
            <p><strong>Title:</strong> {movie.title}</p>
            <p><strong>Original Title:</strong> {movie.original_title}</p>
            <p><strong>Year:</strong> {movie.year}</p>
            <p><strong>Date Published:</strong> {movie.date_published}</p>
            <p><strong>Genres:</strong> {movie.genres}</p>
            <p><strong>Duration:</strong> {movie.duration}</p>
            <p><strong>Country:</strong> {movie.country}</p>
            <p><strong>Language:</strong> {movie.language}</p>
            <p><strong>Director:</strong> {movie.director}</p>
            <p><strong>Writer:</strong> {movie.writer}</p>
            <p><strong>Production Company:</strong> {movie.production_company}</p>
            <p><strong>Actors:</strong> {movie.actors}</p>
            <p><strong>Description:</strong> {movie.description}</p>
            <p><strong>Avg Vote:</strong> {movie.avg_vote}</p>
            <p><strong>Votes:</strong> {movie.votes}</p>
            <p><strong>Budget:</strong> {movie.budget}</p>
            <p><strong>USA Gross:</strong> {movie.us_gross}</p>
            <p><strong>Worldwide Gross:</strong> {movie.worldwide_gross}</p>
            <p><strong>Metascore:</strong> {movie.metascore}</p>
            <p><strong>Reviews from users:</strong> {movie.reviews_from_users}</p>
            <p><strong>Reviews from critics:</strong> {movie.reviews_from_critics}</p>
          </div>
        ))
      ) : (
        <p className="no-movies-message">There are not movies with that title.</p>
      )}
    </div>
  );
};

export default MovieList;
