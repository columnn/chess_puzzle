parent(pam, bob).
parent(tom, bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(joe,jim).

male(tom).
male(bob).
male(joe).
male(jim).

female(pam).
female(liz).
female(ann).
female(pat).

%son/2, granddaughter/2, aunt/2, partner/2

son(X,Y) :- parent(Y,X), male(X).

granddaughter(X,Y) :- parent(Y,Z), parent(Z,X), female(X).

aunt(X,Y) :- parent(Z,X), parent(Z,W), parent(W,Y), female(X), not(X=W).

partner(X,Y) :- parent(X,Z), parent(Y,Z), not(X=Y).