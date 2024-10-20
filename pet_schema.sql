CREATE TABLE IF NOT EXISTS pets (
    PetID TEXT PRIMARY KEY,
    PetType TEXT,
    Breed TEXT,
    AgeMonths INTEGER,
    Color TEXT,
    Size TEXT,
    WeightKg REAL,
    Vaccinated INTEGER,
    HealthCondition INTEGER,
    TimeInShelterDays INTEGER,
    AdoptionFee REAL,
    PreviousOwner INTEGER,
    AdoptionLikelihood INTEGER
);

