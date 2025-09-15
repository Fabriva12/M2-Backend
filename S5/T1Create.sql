-- SQLite
-- Cree el esquema nuevo
CREATE SCHEMA lyfter_car_rental;

-- La tabla
CREATE TABLE lyfter_car_rental.Users(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
Name VARCHAR(30) NOT NULL,
Email VARCHAR(35) NOT NULL,
Username VARCHAR(30) NOT NULL,
Pasword VARCHAR(15) NOT NULL,
Birthdate VARCHAR(10) NOT NULL,
Count_State VARCHAR (15) NOT NULL
);

insert into Users (name, birthdate, email, Pasword, Username, Count_State) 
values 
    ('Kimmi Tuvey', '10/28/1965', 'ktuvey0@ucoz.ru', 'wU7|"."', 'ktuvey0', 'inactiva'),
    ('Aubry Swaffer', '02/15/1991', 'aswaffer1@biblegateway.com', 'fZ6$rPM{', 'aswaffer1', 'activa'),
    ('Lorette Belison', '09/18/1956', 'lbelison2@theglobeandmail.com', 'vG3@', 'lbelison2', 'activa'),
    ('Henryetta Haukey', '12/24/1999', 'hhaukey3@posterous.com', 'cV4=LM6j', 'hhaukey3', 'inactiva'),
    ('Leonhard Maior', '02/25/2002', 'lmaior4@163.com', 'lV4?2lX', 'lmaior4', 'activa'),
    ('Betteann Jirsa', '03/25/1972', 'bjirsa5@mapquest.com', 'bJ9>LvQm', 'bjirsa5', 'activa'),
    ('Donnell Climson', '11/03/2005', 'dclimson6@mozilla.org', 'xS7%G', 'dclimson6', 'inactiva'),
    ('Katie Whichelow', '11/15/1986', 'kwhichelow7@pinterest.com', 'yN7''7!', 'kwhichelow7', 'inactiva'),
    ('Gran Vanetti', '07/26/1991', 'gvanetti8@cisco.com', 'zT4{>/_', 'gvanetti8', 'activa'),
    ('Sisile Belhomme', '09/17/2005', 'sbelhomme9@google.fr', 'xZ0"''}_', 'sbelhomme9', 'activa'),
    ('Harris Hartwright', '09/28/1983', 'hhartwrighta@slate.com', 'hO3''6''', 'hhartwrighta', 'inactiva'),
    ('Lenci Spary', '08/04/1981', 'lsparyb@technorati.com', 'mD4`r', 'lsparyb', 'inactiva'),
    ('Regen Halgarth', '08/03/2004', 'rhalgarthc@google.ca', 'zW6{/z', 'rhalgarthc', 'activa'),
    ('Warden Eagling', '08/26/1959', 'weaglingd@state.gov', 'hS8(a_K', 'weaglingd', 'activa'),
    ('Arlana McGiff', '02/04/2003', 'amcgiffe@squidoo.com', 'bS8#', 'amcgiffe', 'inactiva'),
    ('Angeli Staziker', '06/25/1966', 'astazikerf@timesonline.co.uk', 'tM0??%', 'astazikerf', 'activa'),
    ('Tedd Harrowing', '09/30/1984', 'tharrowingg@boston.com', 'sQ4|D', 'tharrowingg', 'inactiva'),
    ('Katherine Meace', '07/07/1970', 'kmeaceh@tuttocitta.it', 'hI0/', 'kmeaceh', 'inactiva'),
    ('Muffin Ireland', '03/19/1964', 'mirelandi@tamu.edu', 'kA0%!!X', 'mirelandi', 'activa'),
    ('Dorolisa Brandsen', '06/16/2000', 'dbrandsenj@phpbb.com', 'wJ0<>J', 'dbrandsenj', 'activa'),
    ('Catlee Stotherfield', '05/14/1961', 'cstotherfieldk@dailymail.co.uk', 'iZ0<9', 'cstotherfieldk', 'activa'),
    ('Danella Frisch', '03/03/1995', 'dfrischl@disqus.com', 'xZ8)ZJdg', 'dfrischl', 'inactiva'),
    ('Damara Suller', '01/12/1994', 'dsullerm@ucoz.ru', 'jT6%z>', 'dsullerm', 'activa'),
    ('Nerta Daw', '06/21/1997', 'ndawn@aboutads.info', 'mV8"l$yE', 'ndawn', 'activa'),
    ('Daveta Gouda', '10/30/2001', 'dgoudao@theguardian.com', 'qR8$', 'dgoudao', 'activa'),
    ('Gayel Baseley', '01/15/1977', 'gbaseleyp@google.pl', 'pG9~Q''t', 'gbaseleyp', 'activa'),
    ('Jason Nottingham', '09/25/1981', 'jnottinghamq@amazon.de', 'kE0_)mU', 'jnottinghamq', 'inactiva'),
    ('Gwennie Dorken', '11/14/2003', 'gdorkenr@alexa.com', 'xJ5?}F+', 'gdorkenr', 'activa'),
    ('Marisa Strothers', '01/18/1958', 'mstrotherss@naver.com', 'nL2(3wP', 'mstrotherss', 'inactiva'),
    ('Maurita Osler', '12/02/1994', 'moslert@com.com', 'jD9_Z=pW', 'moslert', 'activa'),
    ('Raffarty Paler', '06/04/1957', 'rpaleru@wired.com', 'qT4??M', 'rpaleru', 'inactiva'),
    ('Corinne Kabsch', '01/17/1957', 'ckabschv@nih.gov', 'cW5\%d&V', 'ckabschv', 'activa'),
    ('Davey Jaffa', '04/09/2003', 'djaffaw@prnewswire.com', 'nQ5/', 'djaffaw', 'inactiva'),
    ('Beverly Spurr', '01/02/1988', 'bspurrx@apache.org', 'iF1(Jr', 'bspurrx', 'activa'),
    ('Bernice Spelman', '03/29/1969', 'bspelmany@cdbaby.com', 'wX4.++.$', 'bspelmany', 'activa'),
    ('Crissie Stark', '09/30/1984', 'cstarkz@list-manage.com', 'xB6,Yt!5', 'cstarkz', 'inactiva'),
    ('Sigfried MacCallion', '05/11/1986', 'smaccallion10@hp.com', 'kM5\?', 'smaccallion10', 'activa'),
    ('Oliver Greenway', '03/02/1990', 'ogreenway11@rediff.com', 'oQ2>TDT', 'ogreenway11', 'inactiva'),
    ('Pris Cluet', '10/19/1961', 'pcluet12@unc.edu', 'kA1{wTQ', 'pcluet12', 'inactiva'),
    ('Konstance Phifer', '01/29/1958', 'kphifer13@sciencedaily.com', 'cH4*', 'kphifer13', 'inactiva'),
    ('Isabelita Ferrarotti', '01/12/1992', 'iferrarotti14@is.gd', 'tE5|', 'iferrarotti14', 'inactiva'),
    ('Octavia Calder', '11/18/2003', 'ocalder15@bloglines.com', 'kG5?E', 'ocalder15', 'inactiva'),
    ('Jocko Reyne', '03/12/1961', 'jreyne16@devhub.com', 'nQ8|2yw/', 'jreyne16', 'inactiva'),
    ('Roselia Buckler', '07/03/1979', 'rbuckler17@typepad.com', 'fQ9"s', 'rbuckler17', 'inactiva'),
    ('Marilyn Somerlie', '04/06/1992', 'msomerlie18@google.cn', 'iJ2>', 'msomerlie18', 'activa'),
    ('Ade Earland', '09/04/1985', 'aearland19@army.mil', 'pI1`7', 'aearland19', 'inactiva'),
    ('Dierdre Lankham', '04/08/1981', 'dlankham1a@yellowbook.com', 'yM9&', 'dlankham1a', 'activa'),
    ('Jessi Tetford', '02/24/1982', 'jtetford1b@tamu.edu', 'kD9"p/', 'jtetford1b', 'activa'),
    ('Rikki Adkins', '01/14/1971', 'radkins1c@timesonline.co.uk', 'oZ9}L', 'radkins1c', 'activa'),
    ('Babette Craise', '06/17/1957', 'bcraise1d@hatena.ne.jp', 'hA4/|9', 'bcraise1d', 'inactiva');

-- Tabla cars
CREATE TABLE lyfter_car_rental.Cars(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
Brand VARCHAR(20) NOT NULL,
Model VARCHAR(20) NOT NULL,
Year VARCHAR(10) NOT NULL,
State VARCHAR (15) NOT NULL
);

insert into lyfter_car_rental.Cars(Brand, Model, Year, State) 
values 
    ('Ford', 'Bronco', 1993, 'rented'),
('Mazda', 'MPV', 2006, 'in repair'),
('Honda', 'Pilot', 2006, 'rented'),
('Nissan', 'Sentra', 1997, 'in repair'),
('Saturn', 'VUE', 2005, 'available'),
('Mazda', 'Miata MX-5', 2000, 'available'),
('Infiniti', 'I', 1999, 'in repair'),
('Lexus', 'LX', 2000, 'rented'),
('Suzuki', 'Esteem', 1997, 'available'),
('Alfa Romeo', '164', 1993, 'available'),
('BMW', 'X5', 2000, 'available'),
('Jeep', 'Liberty', 2003, 'in repair'),
('Subaru', 'Outback', 2010, 'rented'),
('Chevrolet', 'Suburban 2500', 1999, 'in repair'),
('Infiniti', 'Q', 1993, 'rented'),
('Aston Martin', 'DB9', 2008, 'in repair'),
('Pontiac', 'Sunbird', 1985, 'rented'),
('Infiniti', 'Q', 1995, 'rented'),
('GMC', 'Suburban 1500', 1995, 'in repair'),
('Honda', 'Civic', 1990, 'available'),
('Subaru', 'Brat', 1987, 'rented'),
('Kia', 'Rio', 2011, 'rented'),
('Buick', 'Riviera', 1986, 'rented'),
('Honda', 'Odyssey', 2007, 'available'),
('Pontiac', 'LeMans', 1991, 'available'),
('Dodge', 'Charger', 2009, 'rented'),
('Lincoln', 'Town Car', 2005, 'in repair'),
('Nissan', 'Frontier', 2004, 'in repair'),
('Chevrolet', 'Camaro', 1977, 'rented'),
('Scion', 'FR-S', 2013, 'in repair'),
('Mitsubishi', 'Cordia', 1988, 'available'),
('Scion', 'tC', 2006, 'available'),
('Cadillac', 'XLR', 2007, 'in repair'),
('Mercury', 'Grand Marquis', 2011, 'rented'),
('Ford', 'Explorer', 2009, 'available'),
('Mercedes-Benz', 'E-Class', 1986, 'rented'),
('Daewoo', 'Nubira', 1999, 'rented'),
('Dodge', 'Ram 1500', 2005, 'available'),
('Ford', 'F150', 2008, 'in repair'),
('Ford', 'Ranger', 1990, 'available'),
('Audi', 'S4', 2002, 'rented'),
('BMW', 'Z3', 1997, 'rented'),
('Hyundai', 'Equus', 2013, 'available'),
('Land Rover', 'Discovery', 2010, 'available'),
('Nissan', 'Quest', 1993, 'in repair'),
('Toyota', 'RAV4', 2002, 'in repair'),
('Volkswagen', 'CC', 2009, 'rented'),
('GMC', 'Yukon', 1993, 'in repair'),
('Acura', 'TL', 2003, 'rented'),
('Volkswagen', 'Jetta', 2001, 'in repair');

-- Tabla de renta
CREATE TABLE lyfter_car_rental.Rent_Cars(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
Car_ID INT ,
User_ID INt,
Rent_date DATE DEFAULT CURRENT_DATE,
State VARCHAR (15) NOT NULL,
CONSTRAINT fk_Cars
        FOREIGN KEY (Car_ID) 
        REFERENCES lyfter_car_rental.Cars (ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
CONSTRAINT fk_Users
        FOREIGN KEY (User_ID) 
        REFERENCES lyfter_car_rental.Users (ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);