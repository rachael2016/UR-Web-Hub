DROP TABLE IF EXISTS "Buildings";

CREATE TABLE "Buildings" (
    "buildingid" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    PRIMARY KEY("buildingid" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "ElevatorDownRecords";

CREATE TABLE "ElevatorDownRecords" (
    "recordid" INTEGER NOT NULL,
    "buildingid" INTEGER NOT NULL,
    "datetime" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "down" BIT NOT NULL,
    PRIMARY KEY("recordid" AUTOINCREMENT),
    FOREIGN KEY("buildingid") REFERENCES "Buildings"(buildingid) ON DELETE CASCADE
);