from rich.console import Console

console = Console()


def show_banner():

    console.print(
        """
[bold cyan]
=========================================================
                    NETPROBE
             Network Monitoring Toolkit
=========================================================
[/bold cyan]
"""
    )