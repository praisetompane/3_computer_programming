%%% declare variale Func
%%% create functin
   %%% and bound variable Func to it
%%%  i.e. bound the identifier "Func"
%%%         to the value : fun if N == 0 then 1 else {Func N - 1} * N
declare
fun {Func N}
   if N == 0 then 1 else {Func N - 1}*N end
end

{Browse {Func 10}}
{Browse {Func 100}}
%%% The results of these invocations is known as infinite arbitary arithmetic
   %%% the inifinity is limited by the amout of memory the computer has

%%% math equivalient
   %%% 0! = 1
   %%% n! = n(n -)! if n > 0

%%% recursive becasuse, factorial of N is N times factorial of N - 1
%%% i.e. the concept of factorial refernces itself to complete itself
   %%%  i.e. defined in terms of itself