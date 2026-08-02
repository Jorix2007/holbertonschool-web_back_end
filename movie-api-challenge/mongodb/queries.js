// Insert

db.movies.insertOne({
    id: 6,
    title: "Dune",
    genre: "Sci-Fi",
    year: 2021,
    rating: 8.2
});

// Find all

db.movies.find();

// Find Sci-Fi

db.movies.find({
    genre: "Sci-Fi"
});

// Rating >= 8

db.movies.find({
    rating: { $gte: 8 }
});

// Update

db.movies.updateOne(
    { id: 3 },
    {
        $set: {
            rating: 8.3
        }
    }
);

// Delete

db.movies.deleteOne({
    id: 4
});

// Count

db.movies.countDocuments();

// Sort

db.movies.find().sort({
    rating: -1
});
