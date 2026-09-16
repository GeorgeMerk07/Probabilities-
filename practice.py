"""In a city, 40% of the people travel by car, 35% travel by bus, 
and 25% travel by train. It is known that 2% of car users are late to work, 
5% of bus users are late, 
and 1% of train users are late.
If a person chosen at random from the city is found to be late to work, 
what is the probability that this person came by bus?"""

#formula for byase theorem : P(B|L) = P(L|B) * P(B) / P(L)

#Define the Given Probabilities
#1. C = Car, B = Bus, T = Train, L = Late
# P(C) = 0.40 # Probability of traveling by car
# P(B) = 0.35 # Probability of traveling by bus
# P(T) = 0.25 # Probability of traveling by train

class BayesTheoremCalculator:
    def __init__(self, p_priors: dict[str, float], p_conditionals: dict[str, float]):
        self.p_priors = p_priors
        self.p_conditionals = p_conditionals

    def total_probability(self) -> float:
        """Calculate total probability P(B) using the Law of Total Probability."""
        return sum(self.p_priors[event] * self.p_conditionals[event] for event in self.p_priors)

    def posterior_probability(self, target_event: str) -> float:
        """Calculates P(Target | Evidence) using Bayes' Theorem."""
        p_evidence = self.total_probability()
        p_joint = (self.p_conditionals[target_event] * self.p_priors[target_event])
        return p_joint / p_evidence

# Define prior probabilities P(Mode)
if __name__ == "__main__":
    priors = {"car": 0.40, "bus": 0.35, "train": 0.25}

    # Define conditional probabilities P(Late | Mode)
    conditionals = {"car": 0.02, "bus": 0.05, "train": 0.01}

    # Initialize calculator
    bayes = BayesTheoremCalculator(priors, conditionals)

    # Compute total probability of being late P(Late)
    p_late = bayes.total_probability()

    # Compute P(Bus | Late)
    p_bus_given_late = bayes.posterior_probability("bus")

    print(f"Total Probability of being late P(L): {p_late:.4f}")
    print(f"Probabilty of taking the bus given late P(B|L): {p_bus_given_late:.4f} {p_bus_given_late * 100:.1f}%")
         