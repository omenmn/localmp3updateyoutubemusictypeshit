from rich.console import Console

console = Console()


def print_missing(songs):

    if not songs:

        console.print("[green]Everything already downloaded![/green]")
        return

    console.print("\n[bold red]Missing songs:[/bold red]\n")

    for song in songs:
        console.print(f"- {song}")
