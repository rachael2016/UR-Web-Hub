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

DROP TABLE IF EXISTS "GeneralFeedbackReceived";

CREATE TABLE "GeneralFeedbackReceived" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "subject" TEXT NOT NULL,
    "message" TEXT NOT NULL,
    "datetime" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "Courses";

CREATE TABLE "Courses" (
    "id" INTEGER NOT NULL,
    "department" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "professor" TEXT,
    "abbreviation" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "CourseRatingsReceived";

CREATE TABLE "CourseRatingsReceived" (
    "reportid" INTEGER NOT NULL,
    "courseid" INTEGER NOT NULL,
    "rating" INTEGER NOT NULL,
    "semester" TEXT NOT NULL,
    "usefulness" INTEGER NOT NULL,
    "message" TEXT NOT NULL,
    "difficulty" INTEGER NOT NULL,
    "tags" TEXT,
    PRIMARY KEY("reportid" AUTOINCREMENT),
    FOREIGN KEY("courseid") REFERENCES "Courses"(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS "DiningFeedbackReceived";

CREATE TABLE "DiningFeedbackReceived" (
    "reportid" INTEGER NOT NULL,
    "location" TEXT NOT NULL,
    "comment" TEXT NOT NULL,
    PRIMARY KEY("reportid" AUTOINCREMENT)
);