-module(geometry).
-export([area/1]).

% this now start on line five.
area({rectangle, Width, Height}) -> Width * Height;

area({circle, Radius}) -> 3.14159 * Radius * Radius;

area({square, Side}) -> Side * Side.
