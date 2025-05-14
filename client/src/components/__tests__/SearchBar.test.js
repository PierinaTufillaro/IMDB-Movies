import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import SearchBar from "../SearchBar";  

describe("SearchBar", () => {

  it("should render the entry field corrrectly", () => {
    render(<SearchBar searchQuery="" handleSearch={() => {}} />);
    
    // Check that the field is rendered
    expect(screen.getByPlaceholderText(/search by title/i)).toBeInTheDocument();
  });

  it("shows the value of the query search passed as prop", () => {
    render(<SearchBar searchQuery="Inception" handleSearch={() => {}} />);
    
    // Check that the input field shows the correct value
    expect(screen.getByPlaceholderText(/search by title/i).value).toBe("Inception");
  });

  it("call handleSearch with the correct value when input changes", () => {
    const handleSearchMock = jest.fn();
    render(<SearchBar searchQuery="" handleSearch={handleSearchMock} />);
    
    // Simulate a change in the input field
    fireEvent.change(screen.getByPlaceholderText(/search by title/i), {
      target: { value: "Matrix" },
    });

    // Check that handleSearch was called with the correct value
    expect(handleSearchMock).toHaveBeenCalledWith("Matrix");
  });

  it("not calling handleSearch if there is no change in the input", () => {
    const handleSearchMock = jest.fn();
    render(<SearchBar searchQuery="Inception" handleSearch={handleSearchMock} />);
    
    // Do not simulate any change in the input field
    expect(handleSearchMock).not.toHaveBeenCalled();
  });
});

