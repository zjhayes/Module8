# Zachary Hayes


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("How many scores are there? "))
    for i in range(1, num_scores + 1):
        score = input("Enter score #%d: " % i)
        scores_dict[i] = int(score)
    return scores_dict


def average_scores(scores):
    running_score = 0
    for i in range(1, len(scores) + 1):
        running_score += scores[i]
    return running_score / len(scores)


if __name__ == '__main__':
    scores = get_test_scores()
    print('Average scores: ' + str(average_scores(scores)))