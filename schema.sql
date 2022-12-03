DROP TABLE IF EXISTS "Buildings";

CREATE TABLE "Buildings" (
    "buildingid" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "xcoord" INTEGER NOT NULL,
    "ycoord" INTEGER NOT NULL,
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

DROP TABLE IF EXISTS "GeneralFeedbackReceived"

CREATE TABLE "GeneralFeedbackReceived" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "subject" TEXT NOT NULL,
    "message" TEXT NOT NULL,
    "datetime" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)