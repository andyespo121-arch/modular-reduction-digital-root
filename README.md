# Modular Reduction via Digital Root

This repository contains a series of works exploring a simple arithmetic function based on digital roots and modular reduction.

## Definition

The function is defined as:

F(n) = n mod dr(n)

where dr(n) is the digital root of n.

## Key Properties

- The output space is restricted to a small finite set
- The function converges in at most two iterations: F(F(n)) = 0
- The computational cost is extremely low
- Certain values are structurally excluded (e.g., 8 in base 10)

## Repository Contents

- **V1** – Intuitive introduction of the idea  
- **V2** – Formal mathematical framework and structural analysis  
- **V3** – Exploration of possible practical and computational applications  

## Notes

The core idea and underlying mechanism were independently developed by the author.  
The mathematical formalization was refined with the support of assistive tools.

## Author

Andrea Esposito

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

