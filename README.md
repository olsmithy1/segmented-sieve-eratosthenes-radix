Segmented Sieve of Eratosthenes with Radix Sort

This implementation combines the Segmented Sieve of Eratosthenes algorithm with Radix sort to efficiently find prime numbers within a given segment [L, R].
Features

    Sieve of Eratosthenes Efficiency: The sieve_eratosthenes function implements the classic Sieve of Eratosthenes algorithm to mark numbers as prime or not. This method efficiently identifies primes up to the square root of the segment's upper limit (R).

    Segmented Sieve Optimization: The segmented_sieve_radix function takes advantage of the Segmented Sieve approach to sieve prime numbers within the given segment [L, R]. It divides the segment into smaller parts and marks multiples of primes in each segment.

    Radix Sort for Prime Segments: Radix sort is utilized within each segment to efficiently mark numbers as prime or non-prime. This linear-time sorting algorithm optimizes the process for large segments, reducing time complexity.

Usage

To use this implementation, follow these steps:

    Clone the repository:

    bash

git clone https://github.com/yourusername/segmented-sieve-radix.git

Navigate to the project directory:

bash

cd segmented-sieve-radix

Modify the script as needed, setting the desired segment [L, R]:

    Adjust the L and R values in the if __name__ == "__main__": block.

Run the Python script:

bash

    python segmented_sieve_radix.py

        This will print the prime numbers within the segment [L, R].

Example

python

# Example Usage
if __name__ == "__main__":
    L, R = 0, 200
    segment_primes = segmented_sieve_radix(L, R)
    print("Prime numbers in the segment [{}, {}]:".format(L, R), segment_primes)

Attribution

    Sieve of Eratosthenes: The sieve_eratosthenes function is based on the classic algorithm devised by Eratosthenes for prime number detection.

    Segmented Sieve Optimization: The segmented_sieve_radix function implements the Segmented Sieve approach to efficiently find prime numbers within a given segment.

    Radix Sort: Radix sort is utilized within the segmented_sieve_radix function to optimize marking numbers as prime or non-prime within each segment.

Author

    Sean Smith - Initial implementation
