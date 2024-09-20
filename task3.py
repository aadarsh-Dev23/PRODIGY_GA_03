import random
import string

class MarkovChain:
    def __init__(self):
        self.chain = {}

    def train(self, text, n=1):
        """Train the Markov chain model using the provided text."""
        # Normalize text: remove punctuation and make lowercase
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()

        # Create n-grams
        for i in range(len(words) - n):
            key = tuple(words[i:i + n])
            next_word = words[i + n]

            if key not in self.chain:
                self.chain[key] = []
            self.chain[key].append(next_word)

    def generate(self, length=10, seed=None, n=1):
        """Generate new text based on the trained model."""
        if seed is None:
            seed = random.choice(list(self.chain.keys()))

        output = list(seed)
        for _ in range(length):
            key = tuple(output[-n:])
            next_word = random.choice(self.chain.get(key, [""]))  # Choose next word randomly
            output.append(next_word)

        return ' '.join(output)

# Example usage
if __name__ == "__main__":
    # Sample text for training
    text = """
    Markov chains are a mathematical system that undergoes transitions from one state to another 
    on a state space. It is a random process that satisfies the Markov property. A Markov chain 
    is defined by a finite number of states and the probabilities of moving from one state to 
    another. They have applications in various fields such as physics, economics, and biology.
    """

    # Initialize and train the Markov chain
    markov_chain = MarkovChain()
    markov_chain.train(text, n=1)  # You can change n to 2 for bigrams

    # Generate new text
    generated_text = markov_chain.generate(length=20, seed=("state",))
    print("Generated Text:")
    print(generated_text)
