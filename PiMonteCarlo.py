import random


def piMonteCarlo(domain):
  inside = 0

  for _ in range(domain):
    x, y = (random.random(), 
          random.random())
    r = (x ** 2 + y ** 2) ** 0.5
    if r <= 1.0:
      inside += 1
    
  return 4 * (inside / domain)
      
      
if __name__ == "__main__":
  for domain in (10_000, 100_000, 
      1_000_000, 10_000_000,
      100_000_000):
    pi = piMonteCarlo(domain) 
    print(f"Estimate of Pi using {domain:,d}")
    print(f"random points = {pi}")
    print("-----")
  
