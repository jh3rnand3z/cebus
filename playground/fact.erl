-module(fact).
-export([factorial/1, factorial2/1]).

factorial(N) when N>1 ->
	io:format("Calling from ~w. ~n", [N]),
	Result = N * factorial(N-1),
	io:format("~w yields ~w. ~n", [N, Result]),
	Result;

factorial(N) when N =< 1 ->
	io:format("Calling from 1. ~n"),
	io:format("1 yields 1. ~n"),
	1.

factorial2(N) ->
	factorial2(1, N, 1).

factorial2(Current, N, Result) when Current =< N ->
	NewResult = Result * Current,
	io:format("~w yields ~w!~n", [Current, NewResult]),
	factorial2(Current+1, N, NewResult);

factorial2(Current, N, Result) ->
	io:format("Finished.~n").