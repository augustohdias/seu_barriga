import bot.seu_barriga
import concurrent.futures

def main():
    tasks = [bot.seu_barriga.notice_billing, bot.seu_barriga.read_updates]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()
    
if __name__ == "__main__":
    main()