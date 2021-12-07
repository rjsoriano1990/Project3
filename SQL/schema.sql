CREATE TABLE "us_gas_prices_region" (
    "ID" SERIAL PRIMARY KEY,
    "date" date   NOT NULL,
    "east_coast" float   NOT NULL,
    "new_england" float   NOT NULL,
    "central_atlantic" float   NOT NULL,
    "lower_atlantic" float   NOT NULL,
    "midwest" float   NOT NULL,
    "gulf_coast" float   NOT NULL,
    "rocky_mountains" float   NOT NULL,
    "west_coast" float   NOT NULL
);