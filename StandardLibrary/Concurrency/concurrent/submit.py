import concurrent.futures as cf 


def main():
    with cf.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())
        
if __name__ == "__main__":
    main()
