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