def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p] == True:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        remaining_numbers = set(range(1, n + 1))
        maria_turn = True
        
        while True:
            made_move = False
            for prime in primes:
                if prime in remaining_numbers:
                    made_move = True
                    multiples = set(range(prime, n + 1, prime))
                    remaining_numbers -= multiples
                    break
            
            if not made_move:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            maria_turn = not maria_turn
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

