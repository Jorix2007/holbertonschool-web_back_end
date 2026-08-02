const movies = [
    ...
];

// Spread

const newMovie = {
    id: 6,
    title: "Dune",
    genre: "Sci-Fi",
    year: 2021,
    rating: 8.2
};

const updatedMovies = [...movies, newMovie];

// Arrow Function

const highRatedMovies = movies.filter(movie => movie.rating >= 8);

// Template Literal

console.log(`${movies[0].title} (${movies[0].year}) - Rating: ${movies[0].rating}`);
