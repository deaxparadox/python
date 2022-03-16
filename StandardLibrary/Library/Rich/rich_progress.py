from rich.progress import track
from time import sleep

def process_data():
    # print("a")
    sleep(0.1)
    
def main():
    for _ in track(range(100), description='[green]Processing data'):
        process_data()
    

main()