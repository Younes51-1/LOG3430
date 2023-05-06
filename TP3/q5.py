from fuzzingbook.MutationFuzzer import MutationFuzzer
from fuzzingbook.Coverage import Coverage
from fuzzingbook.Fuzzer import Fuzzer, RandomFuzzer
from num2words import num2words
import random
import matplotlib.pyplot as plt

random.seed(2134091)


class MyFuzzer(Fuzzer):
    def __init__(self):
        self.min = -9 * 10**10
        self.max = 9 * 10**10

    def fuzz(self):
        return random.uniform(self.min, self.max)


def calculate_cumulative_coverage(input_population, function):
    cumulative_coverage = []
    all_coverage = set()
    
    for inp in input_population:
        with Coverage() as cov:
            try:
                function(inp)
            except:
                # we ignore exceptions for the purpose of this code, but some exceptions may be interesting
                pass
        # set union
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))
    return cumulative_coverage


def plot(cumulative_coverage, fuzzer_type):
    plt.plot(cumulative_coverage, label=fuzzer_type)
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")


trials = 500
randomFuzzer = RandomFuzzer()
mutationFuzzer = MutationFuzzer(seed=["3452020"])
myFuzzer = MyFuzzer()


def fuzzer_coverage(fuzzer):
    input_set = []
    for i in range(0, trials):
        input_set.append(fuzzer.fuzz())
    return calculate_cumulative_coverage(input_set, num2words)


plot(fuzzer_coverage(randomFuzzer), "randomFuzzer")
plot(fuzzer_coverage(mutationFuzzer), "mutationFuzzer")
plot(fuzzer_coverage(myFuzzer), "myFuzzer")
plt.tight_layout()
plt.show()

