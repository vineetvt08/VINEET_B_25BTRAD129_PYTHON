import string

class FrequencyCounter:
    def __init__(self):
        pass

    def count_words(self, sentence):
        """Count word frequencies in a sentence (case-insensitive, ignoring punctuation)."""
        # Remove punctuation and convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        cleaned_sentence = sentence.translate(translator).lower()
        words = cleaned_sentence.split()

        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
        return freq_dict

    def count_elements(self, elements_list):
        """Count occurrences of elements in a list."""
        freq_dict = {}
        for item in elements_list:
            # Normalize strings to lowercase/strip whitespace for clean counting
            normalized_item = str(item).strip().title()
            freq_dict[normalized_item] = freq_dict.get(normalized_item, 0) + 1
        return freq_dict

    def display_frequency(self, freq_dict, title="Frequency Report"):
        """Display the frequency dictionary in a clean tabular layout."""
        if not freq_dict:
            print("\n[Info] No data to display.")
            return

        print("\n" + "=" * 45)
        print(f" {title.upper()} ")
        print("=" * 45)
        print(f"{'ELEMENT / WORD':<25} | {'FREQUENCY':<10}")
        print("-" * 45)

        # Sort by frequency in descending order for better analytical insight
        sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        for item, count in sorted_freq:
            print(f"{item:<25} | {count:<10}")
        print("=" * 45 + "\n")

def main():
    counter = FrequencyCounter()

    # Pre-loaded Real-World Scenario Data: Product Preference Survey Responses
    survey_responses = [
        "Smartphone", "Laptop", "Tablet", "Smartphone", "Headphones",
        "Laptop", "Smartphone", "Smartwatch", "Tablet", "Smartphone",
        "Headphones", "Laptop", "Smartwatch", "Smartphone", "Tablet"
    ]

    while True:
        print("\n--- FREQUENCY COUNTER MENU ---")
        print("1. Count Word Frequencies in a Sentence")
        print("2. Analyze Product Preference Survey (Pre-loaded Data)")
        print("3. Input Custom List of Elements")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            sentence = input("Enter a sentence or paragraph: ").strip()
            if sentence:
                result = counter.count_words(sentence)
                counter.display_frequency(result, "Word Frequency Analysis")
            else:
                print("\n[Error] Input cannot be empty.")

        elif choice == '2':
            print("\n[Scenario] Analyzing E-Commerce Product Preference Survey Responses...")
            result = counter.count_elements(survey_responses)
            counter.display_frequency(result, "Product Preference Survey Results")
            print("Interpretation: 'Smartphone' is the most preferred product category, followed by 'Laptop' and 'Tablet'.")

        elif choice == '3':
            raw_input_str = input("Enter items separated by commas (e.g., Apple, Banana, Apple): ").strip()
            if raw_input_str:
                items = [item.strip() for item in raw_input_str.split(",")]
                result = counter.count_elements(items)
                counter.display_frequency(result, "Custom List Frequency Analysis")
            else:
                print("\n[Error] Input cannot be empty.")

        elif choice == '4':
            print("\nExiting Frequency Counter. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
