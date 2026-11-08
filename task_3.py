import heapq


def min_cost(cables):
    """Мінімальні витрати на об'єднання кабелів.

    Щоразу беремо два найкоротші кабелі, з'єднуємо їх
    і кладемо результат назад у купу.
    """
    heap = list(cables)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        joined = first + second
        total += joined
        heapq.heappush(heap, joined)
    return total


def main():
    cables = [4, 3, 2, 6]
    print("Кабелі:", cables)
    print("Мінімальні витрати:", min_cost(cables))
    print("Один кабель:", min_cost([5]))


if __name__ == "__main__":
    main()
