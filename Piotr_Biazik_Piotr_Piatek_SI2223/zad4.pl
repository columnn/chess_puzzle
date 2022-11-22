len([],0).
len([_|T],N) :- len(T,Z), N is Z + 1.

rlen([],zero).
rlen([H|T],N) :- rlen(H,X), rlen(T,Y), !, add(X,Y,N).
rlen(_,s(zero)).

concat([],X,X).
concat([H|T], X, [H|Y]) :- concat(T,X,Y).

reverse1([],[]).
reverse1([H|T],Q) :- reverse1(T,X), concat(X,[H],Q).

reverse2([],X,X).
reverse2([H|T], X, Q) :- reverse2(T, [H|X], Q).

sum([],0).
sum([H|T],N) :- sum(T,X), N is X + H.

avg([],_) :- !, false.
avg(X,N) :- sum(X,S), len(X,L), N is round(S / L).

count(_, [], 0).
count(H, [H|T], N) :- !, count(H, T, Q), N is Q + 1.
count(X, [_|T], N) :- count(X, T, N).

double([],[]).
double([H|T1],[H|[H|T2]]) :-  double(T1,T2).

repeat([],[],_). 
repeat([H|T],L,N) :- repeat(T,L2,N), repeat2(H,L1,N), concat(L1,L2,L).
repeat2(_,[], 0).
repeat2(H, [H|T], N) :- Q is N - 1, repeat2(H, T, Q), !. 