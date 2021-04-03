# Negative vs Positive

def negative_vs_positive(a_list):
    negatives = sum(list(filter(lambda x: x < 0, a_list)))
    positives = sum(list(filter(lambda x: x >= 0, a_list)))
    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


a_list = [int(num) for num in input().split()]
negative_vs_positive(a_list)
