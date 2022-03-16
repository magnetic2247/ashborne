insert into Profs (id_prof, nom_prof, pre_prof) values
    ("GAJé", "GAUTHIER", "Jérôme"),
    ("ROFr", "ROMPTEAUX", "Freddy"),
    ("MACa", "MAZEAU", "Caroline"),
    ("HEJu", "HERNANDEZ", "Juan")
;

insert into Options (id_option, matiere_option, id_prof) values
    ("M1", "MATHS", "GAJé"),
    ("M2", "MATHS", "GAJé"),
    ("H1", "HISTOIRE", "ROFr"),
    ("H2", "HISTOIRE", "ROFr"),
    ("A1", "ANGLAIS", "MACa"),
    ("E1", "ESPAGNOL", "HEJu")
;

insert into Eleves (id_eleve, nom_eleve, pre_eleve, dnd_eleve, id_option) values
    ("BOWa0501", "BOURGY", "Wael", "12/05/2001", "M1"),
    ("DEAl0700", "DESSENS", "Alexandre", "05/07/2000", "M2"),
    ("OMLo1201", "OMAIS", "Loana", "15/12/2001", "H1"),
    ("DEMa0101", "DESVAUX", "Margaux", "25/01/2001", "A1"),
    ("DEVi0700", "DESSENS", "Vincent", "05/07/2000", "E1"),
    ("PADa1200", "PAYEN", "Damiens", "28/12/2000", "H1"),
    ("GAAx0301", "GARNIER", "Axelle", "14/03/2001", "H2")
;