isnumber(zero).
isnumber(s(X)) :- isnumber(X).

isequal(X,X) :- isnumber(X).
isequal(s(X),s(Y)) :- isequal(X,Y).

lessthanequal(zero,X) :- isnumber(X).
lessthanequal(s(X),s(Y)) :- lessthanequal(X,Y).

add(zero,X,X) :- isnumber(X).
add(s(X),Y,s(Z)) :- add(X,Y,Z).

even(zero).
even(s(X)) :- odd(X).
odd(s(X)) :- even(X).

times(zero,X,zero) :- isnumber(X).
times(s(X),Y,Z) :- times(X,Y,Q), add(Y,Q,Z).

quotient(_,zero,_) :- false.
quotient(X,Y,Q) :- times(Q,Y,X).

remainder(X,Y,R) :- lessthanequal(X,Y), R=X.
remainder(zero,_, zero).
remainder(_, zero, _) :- false.
remainder(X,Y,R) :- add(Y,Q,X),write(Q),remainder(Q,Y,R).

fact(zero,s(zero)).
fact(s(N),X) :- fact(N,Q), quotient(X,s(N),Q).

fibonacci(zero,zero).
fibonacci(s(zero),s(zero)).
fibonacci(s(s(zero)),s(zero)).
fibonacci(s(s(N)), X) :- fibonacci(s(N), Q), fibonacci(N, Y), add(Q,Y,X).

shownum(zero,0).
shownum(s(X),Y) :- shownum(X,Q), Y is Q + 1.