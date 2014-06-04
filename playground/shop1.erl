-module(shop1).
-export([total/1]).

%  Buy = [{oranges,4}, {newspaper,1}, {apples,10}, {pears,6}, {milk,3}].

total([{What, N}|T]) -> shop:cost(What) * N + total(T);

total([]) -> 0.