function com = combinations(n,k)
% COMBINATIONS calculates the number of ways you may choose k elements from
% n elements. For example, you can choose 2 elements from 3 elements in
% 3!/(2!(3-2)!) = 3 ways
    if k > n
        error('Cannot calculate with given values')
    end
    com = factorial(n)/(factorial(k)*factorial(n-k));
end