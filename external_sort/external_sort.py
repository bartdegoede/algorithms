import asyncio
import heapq
import random


async def sort_chunk(chunk: list[int]) -> list[int]:
    """Sort a chunk of integers in descending order. Descending order because
    then we can use .pop() on the list to get the smallest element."""
    return sorted(chunk, reverse=True)


async def external_sort(nums: list[int], parallelism: int = 25) -> list[int]:
    """Sort a list of integers using external sort."""
    # Split the list into chunks
    chunk_size = len(nums) // parallelism
    chunks = [nums[i : i + chunk_size] for i in range(0, len(nums), chunk_size)]
    assert len(chunks) == parallelism

    # sort in parallel
    tasks: list[asyncio.Task] = [
        asyncio.create_task(sort_chunk(chunk)) for chunk in chunks
    ]
    sorted_subarrays = await asyncio.gather(*tasks)
    assert sum(len(subarray) for subarray in sorted_subarrays) == len(nums)

    result = []
    heap: list[tuple[int, int]] = []
    for subarray_index, subarray in enumerate(sorted_subarrays):
        heapq.heappush(heap, (subarray.pop(), subarray_index))

    while heap:
        smallest_value, subarray_index = heapq.heappop(heap)

        if sorted_subarrays[subarray_index]:
            heapq.heappush(
                heap, (sorted_subarrays[subarray_index].pop(), subarray_index)
            )

        result.append(smallest_value)

    assert len(result) == len(nums)
    return result


if __name__ == "__main__":
    numbers = list(range(1, 1000001))
    random.shuffle(numbers)

    sorted_numbers = asyncio.run(external_sort(numbers, parallelism=100))
    assert sorted_numbers == sorted(numbers)
