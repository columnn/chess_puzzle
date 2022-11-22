parent(janina, anna).
parent(edward, anna).
parent(wilhemina, andrzej).
parent(marian, andrzej).
parent(anna, magdalena).
parent(anna, tomasz).
parent(andrzej, magdalena).
parent(andrzej, tomasz).
parent(tomasz, zuzanna).
parent(karolina, zuzanna).

male(edward).
male(andrzej).
male(marian).
male(tomasz).

female(janina).
female(wilhemina).
female(anna).
female(magdalena).
female(karolina).
female(zuzanna).

mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(X).

child(X,Y):- parent(Y,X).

grandparent(X,Y):- parent(X,Z), parent(Z,Y).

greatgrandparent(X,Y):- grandparent(X,Z), parent(Z,Y).

son(X,Y):- parent(Y,X), male(X).

granddaughter(X,Y):- grandparent(Y,X), female(X).

aunt(X,Y):- parent(Z,X), parent(Z,W), parent(W,Y), female(X), not(X=W).

partner(X,Y):- child(Z,X), child(Z,Y).

ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z), ancestor(Z,Y).

descendant(X,Y):- child(X,Y).
descendant(X,Y):- child(X,Z), descendant(Z,Y).