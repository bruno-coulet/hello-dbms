-- Création de la base de données
CREATE DATABASE IF NOT EXISTS UEFA_EURO_2012;
USE UEFA_EURO_2012;

-- Table Game
CREATE TABLE Game (
    id INT PRIMARY KEY,
    mdate DATE,
    stadium VARCHAR(255),
    team1 CHAR(3),
    team2 CHAR(3)
);

-- Table Goal
CREATE TABLE Goal (
    matchid INT,
    teamid CHAR(3),
    player VARCHAR(255),
    gtime INT,
    FOREIGN KEY (matchid) REFERENCES Game(id)
);

-- Table Eteam
CREATE TABLE Eteam (
    id CHAR(3) PRIMARY KEY,
    teamname VARCHAR(255),
    coach VARCHAR(255)
);

INSERT INTO Game (id, mdate, stadium, team1, team2) VALUES
(1001, '2012-06-08', 'National Stadium, Warsaw', 'POL', 'GRE'),
(1002, '2012-06-08', 'Stadion Miejski (Wroclaw)', 'RUS', 'CZE'),
(1003, '2012-06-12', 'Stadion Miejski (Wroclaw)', 'GRE', 'CZE'),
(1004, '2012-06-12', 'National Stadium, Warsaw', 'POL', 'RUS');

INSERT INTO Goal (matchid, teamid, player, gtime) VALUES
(1001, 'POL', 'Robert Lewandowski', 17),
(1001, 'GRE', 'Dimitris Salpingidis', 51),
(1002, 'RUS', 'Alan Dzagoev', 15),
(1002, 'RUS', 'Roman Pavlyuchenko', 82);

INSERT INTO Eteam (id, teamname, coach) VALUES
('POL', 'Poland', 'Franciszek Smuda'),
('RUS', 'Russia', 'Dick Advocaat'),
('CZE', 'Czech Republic', 'Michal Bilek'),
('GRE', 'Greece', 'Fernando Santos');

SELECT matchid, player 
FROM Goal 
WHERE teamid = 'GER';

SELECT id, stadium, team1, team2 
FROM Game 
WHERE id = 1012;

SELECT Goal.player, Goal.teamid, Game.stadium, Game.mdate 
FROM Game 
JOIN Goal ON Game.id = Goal.matchid 
WHERE Goal.teamid = 'GER';

SELECT Game.team1, Game.team2, Goal.player 
FROM Game 
JOIN Goal ON Game.id = Goal.matchid 
WHERE Goal.player LIKE '%Mario%';

SELECT Goal.player, Goal.teamid, Eteam.teamname, Eteam.coach 
FROM Goal 
JOIN Eteam ON Goal.teamid = Eteam.id;

SELECT Goal.player, Goal.teamid, Eteam.coach, Goal.gtime 
FROM Goal 
JOIN Eteam ON Goal.teamid = Eteam.id 
WHERE Goal.gtime <= 10;

SELECT Game.mdate, Eteam.teamname 
FROM Game 
JOIN Eteam ON Game.team1 = Eteam.id 
WHERE Eteam.coach = 'Fernando Santos';

SELECT Goal.player 
FROM Goal 
JOIN Game ON Goal.matchid = Game.id 
WHERE Game.stadium = 'National Stadium, Warsaw';

SELECT teamid, COUNT(*) AS total_goals 
FROM Goal 
GROUP BY teamid;

SELECT Game.stadium, COUNT(*) AS total_goals 
FROM Game 
JOIN Goal ON Game.id = Goal.matchid 
GROUP BY Game.stadium;

SELECT Game.id, Game.mdate, COUNT(Goal.player) AS total_goals 
FROM Game 
JOIN Goal ON Game.id = Goal.matchid 
WHERE Goal.teamid = 'FRA' 
GROUP BY Game.id, Game.mdate;

