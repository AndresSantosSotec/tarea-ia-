% Archivo familia.pl
progenitor(jose, pedro).
progenitor(karla, pedro).
progenitor(jose, carolina).
progenitor(karla, carolina).
progenitor(pedro, mario).

hombre(jose).
hombre(pedro).
hombre(mario).
mujer(carolina).
mujer(karla).

papa(X, Y) :- progenitor(X, Y), hombre(X).
mama(X, Y) :- progenitor(X, Y), mujer(X).

% Definición de la relación hermano
hermano(X, Y) :- progenitor(Z, X), progenitor(Z, Y), X \= Y.
