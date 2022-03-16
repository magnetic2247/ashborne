create table Profs (
    id_prof text not null primary key,
    nom_prof text not null,
    pre_prof text not null
);

create table Options (
    id_option text not null primary key,
    matiere_option text not null,
    id_prof text not null,
    constraint options_fk foreign key (id_prof) references Profs(id_prof)
);

create table Eleves (
    id_eleve text not null primary key,
    nom_eleve text not null,
    pre_eleve text not null,
    dnd_eleve text not null,
    id_option text not null,
    constraint eleve_fk foreign key (id_option) references Options(id_option)
);
