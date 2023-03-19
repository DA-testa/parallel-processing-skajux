# python3
#Kristiās Martiņjaks 221RDB223
def parallel_processing(n, m, data):
    threads = [(i, 0) for i in range(n)]
    output = []
    for i in range(m):
        job_time = data[i]
        thread_index, thread_time = min(threads, key=lambda x: x[1])
        output.append((thread_index, thread_time))
        threads[thread_index] = (thread_index, thread_time + job_time)
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()

