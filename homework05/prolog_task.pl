% Rules
sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.

% Query
?- sum_list([1, 2, 3, 4, 5], Result).