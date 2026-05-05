import collections

def train_and_tag(training_data, test_sentences):
    word_tags = collections.defaultdict(lambda: collections.defaultdict(int))
    for sentence in training_data:
        for word, tag in sentence:
            word_tags[word][tag] += 1
            
    most_freq = {}
    for word, tags in word_tags.items():
        most_freq[word] = max(tags.items(), key=lambda x: x[1])[0]

    results = []
    for sentence in test_sentences:
        tagged = []
        for word in sentence:
            tagged.append((word, most_freq.get(word, 'NN')))
        results.append(tagged)
    return results

if __name__ == "__main__":
    # Example usage
    train = [[("The", "DT"), ("cat", "NN"), ("sat", "VBD")]]
    test = [["The", "dog", "sat"]]
    print(train_and_tag(train, test))
