import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import SearchBar from './components/SearchBar';
import MovieList from './components/MovieList';

describe('App Component', () => {
  it('renders without crashing', () => {
    render(<App />);
        expect(screen.getByText('🎬 Movie Searcher')).toBeInTheDocument();
  });

  it('renders the searchbar crashing', () => {
    render(<SearchBar searchQuery="" handleSearch={() => {}} />);
    
    expect(screen.getByPlaceholderText('Search by title.')).toBeInTheDocument();
  });

  it('renders movie titles when movies are passed', () => {
    const movies = [
      { title: 'Inception', id: 1 },
      { title: 'Interstellar', id: 2 },
    ];

    render(<MovieList movies={movies} currentPage={1} moviesPerPage={12} />);
    
    expect(screen.getByRole('heading', { name: /Inception/i })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: /Interstellar/i })).toBeInTheDocument();
  });
}); 