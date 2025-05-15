import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import App from "./App";

beforeEach(() => {
  jest.spyOn(global, "fetch").mockImplementation(() =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          {
            title: "Movie 1",
            year: 2021,
            genre: "Action",
            director: "Director 1",
            plot: "Plot of Movie 1",
          },
          {
            title: "Movie 2",
            year: 2022,
            genre: "Comedy",
            director: "Director 2",
            plot: "Plot of Movie 2",
          },
          {
            title: "Movie 3",
            year: 2023,
            genre: "Drama",
            director: "Director 3",
            plot: "Plot of Movie 3",
          },
        ]),
    })
  );
});

afterEach(() => {
  jest.restoreAllMocks();
});

describe("App", () => {
  it("should render the main title", () => {
    render(<App />);
    const title = screen.getByText(/movie searcher/i);
    expect(title).toBeInTheDocument();
  });

  it("should display the loader while fetching movies", async () => {
    render(<App />);
    expect(screen.getByText(/loading/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.queryByText(/loading/i)).not.toBeInTheDocument();
    });
  });

  it("should call the movies API on mount", () => {
    render(<App />);
    expect(global.fetch).toHaveBeenCalledWith(
      "http://127.0.0.1:5000/api/movies"
    );
  });

  it("should disable the 'Previous' button on the first page", () => {
    render(<App />);
    const prevButton = screen.getByText(/previous/i);
    expect(prevButton).toBeDisabled();
  });
});
