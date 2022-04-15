CREATE TABLE `Mood`(
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `lable` TEXT NOT NULL
);

CREATE TABLE `Entries` (
    `id`        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept`   TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `date`      DATE NOT NULL,
    `mood_id`   INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Tag` (
    `id`       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`     TEXT NOT NULL 
);

CREATE TABLE `EntryTag` (
    `id`        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id`  INTEGER NOT NULL,
    `tag_id`    INTEGER NOT NULL,
    FOREIGN KEY (`entry_id`) REFERENCES `Entries`(`id`),
    FOREIGN KEY (`tag_id`) REFERENCES `Tag` (`id`)
);

INSERT INTO `Tag` VALUES (null, 'New Concept');
INSERT INTO `Tag` VALUES (null, 'Challenging');
INSERT INTO `Tag` VALUES (null, 'Easy');
INSERT INTO `Tag` VALUES (null, 'Intermediate');
INSERT INTO `Tag` VALUES (null, 'Interesting');
INSERT INTO `Tag` VALUES (null, 'Dull');

SELECT * FROM Tag;

Select * FROM EntryTag;

INSERT INTO `EntryTag` VALUES (null, 1, 1);
INSERT INTO `EntryTag` VALUES (null, 1, 2);

INSERT INTO `Mood` VALUES (null, 'Feelin Angry');
INSERT INTO `Mood` VALUES (null, 'Feelin Content');
INSERT INTO `Mood` VALUES (null, 'Feelin Frustrated');
INSERT INTO `Mood` VALUES (null, 'Feelin Good');
INSERT INTO `Mood` VALUES (null, 'Feelin a lil Sad');

INSERT INTO `Entries` VALUES (null, 'SQL', 'SQL is really hard so far.', '2022-04-11', 3);
INSERT INTO `Entries` VALUES (null, 'Python', 'SO EXCITED to learn Python', '2022-04-08', 4);
INSERT INTO `Entries` VALUES (null, 'Python', 'Learned how to do this thing today. It was hard, but cool.', '2022-04-09', 2);
INSERT INTO `Entries` VALUES (null, 'SQL', 'Did the SQL exercises, and things make more sense now.', '2022-04-08', 4);
INSERT INTO `Entries` VALUES (null, 'Python', 'Let myself get stuck for way too long. Should have asked for help sooner.', '2022-04-11', 5);


SELECT * FROM  entries

SELECT * FROM mood

DELETE FROM entries
WHERE id = 1

SELECT * FROM Entries
WHERE entry LIKE '%python%'

SELECT * 
FROM Entries e 
JOIN Mood m ON e.mood_id = m.id

SELECT
    e.id,
    et.id,
    et.entry_id,
    et.tag_id,
    t.id,
    t.name
FROM entries e
JOIN entrytag et
    ON e.id = et.entry_id
JOIN tag t
    ON t.id = et.tag_id  
