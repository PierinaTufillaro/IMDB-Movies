import React from "react";
import { render, screen } from "@testing-library/react";
import MovieList from "../MovieList";

const sampleMovies = [
    {
      id: 1,
      title: "The Matrix",
      original_title: "The Matrix",
      year: 1999,
      genre: "Action",
      description: "A hacker discovers reality is a simulation.",
      director: "Lana Wachowski, Lilly Wachowski",
      actors: "Keanu Reeves, Laurence Fishburne",
      avg_vote: 8.7,
      imdb_title_id: "tt0133093",
      date_published: "1999-03-31",
      genres: "Action, Sci-Fi",
      duration: "136",
      country: "USA",
      language: "English",
      writer: "Lana Wachowski",
      production_company: "Warner Bros.",
      votes: "1000000",
      budget: "$63,000,000",
      us_gross: "$171,479,930",
      worldwide_gross: "$463,517,383",
      metascore: "73",
      reviews_from_users: "2000",
      reviews_from_critics: "300"
    },
    {
      id: 2,
      title: "Inception",
      original_title: "Inception",
      year: 2010,
      genre: "Sci-Fi",
      description: "A thief enters dreams to steal secrets.",
      director: "Christopher Nolan",
      actors: "Leonardo DiCaprio, Joseph Gordon-Levitt",
      avg_vote: 8.8,
      imdb_title_id: "tt1375666",
      date_published: "2010-07-16",
      genres: "Action, Sci-Fi, Thriller",
      duration: "148",
      country: "USA",
      language: "English",
      writer: "Christopher Nolan",
      production_company: "Warner Bros.",
      votes: "2000000",
      budget: "$160,000,000",
      us_gross: "$292,576,195",
      worldwide_gross: "$836,800,000",
      metascore: "74",
      reviews_from_users: "3500",
      reviews_from_critics: "500"
    }
  ];  

describe("MovieList", () => {
  it("Render the movies send by props", () => {
    render(<MovieList movies={sampleMovies} currentPage={1} moviesPerPage={10} />);

    expect(screen.getByRole("heading", { name: /The Matrix/i })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Inception/i })).toBeInTheDocument();

    expect(screen.getByText(/A hacker discovers reality is a simulation./i)).toBeInTheDocument();
    expect(screen.getByText(/A thief enters dreams to steal secrets./i)).toBeInTheDocument();
    });

  it("Shows only the movies on the current page", () => {
    render(<MovieList movies={sampleMovies} currentPage={1} moviesPerPage={1} />);
    expect(screen.getByRole("heading", { name: /The Matrix/i })).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Inception/i })).not.toBeInTheDocument();
  });
});
