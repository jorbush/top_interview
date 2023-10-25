-module(solution).
-export([is_valid/1]).

is_valid(S) ->
    is_valid(S, []).

is_valid([], Stack) ->
    Stack == [];
is_valid([H|T], Stack) when H == $) orelse H == $] orelse H == $} ->
    case Stack of
        [] -> false;
        [Hs|TStack] when match(Hs, H) -> is_valid(T, TStack);
        _ -> false
    end;
is_valid([H|T], Stack) when H == $($ orelse H == $[ orelse H == ${ ->
    is_valid(T, [H|Stack]).

match($), $($) -> true;
match($], $[) -> true;
match($}, ${) -> true;
match(_, _) -> false.