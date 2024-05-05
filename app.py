import click
from rich.console import Console
from openai import OpenAI, OpenAIError
from tqdm import tqdm  # Import tqdm for progress bars

# Set up your OpenAI API Key as an environment variable 'OPENAI_API_KEY'
client = OpenAI()
console = Console()

@click.command()
@click.option("--image_url", prompt="Enter image URL", help="The URL of the image to analyze.")
def analyze_image(image_url):
    """Analyzes an image and generates multiple refined HTML outputs, then merges them, showing progress with tqdm."""
    try:
        # Initialize the detailed description prompt
        initial_prompt = """
        Analyze this image and provide a comprehensive description that includes:
        - Color schemes and their significance.
        - Layout and structural elements, including any navigational features.
        - Textual content verbatim where applicable.
        - Any symbolic or graphical elements and their potential implications.
        - Accessibility considerations important for a blind person to understand the website's content and structure.
        """
        
        prompt = initial_prompt  # Start with the initial comprehensive prompt
        html_versions = []  # List to store each iteration's HTML output

        # Generate HTML outputs in multiple iterations with progress display
        for i in tqdm(range(5), desc="Generating descriptions and HTML"):
            description_response = client.chat.completions.create(
                model="gpt-4-1106-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": image_url}},
                        ],
                    }
                ],
                max_tokens=3000,
            )

            # Update the prompt with the latest description for further refinement
            prompt = description_response.choices[0].message.content
            console.print(f"[bold blue]Iteration {i+1} - Image Description:[/bold blue]")
            console.print(prompt)

            # Generate HTML for the current description
            html_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate a complete MVP including CDNs for styling and all HTML representation based on the following website design description. DO NOT INCLUDE EXPLANATIONS AS THIS WILL BE FED INTO A MACHINE: {prompt}"
                    }
                ],
                max_tokens=6500
            )
            # Store HTML output for this iteration
            html_versions.append(html_response.choices[0].message.content)
            console.print(f"[bold green]Iteration {i+1} - Generated HTML:[/bold green]")
            console.print(html_versions[-1])

        # Final merging of all HTML iterations
        final_html = "\n".join(html_versions)  # Simple concatenation for merging
        console.print("[bold magenta]Final Merged HTML:[/bold magenta]")
        console.print(final_html)

    except OpenAIError as e:
        console.print(f"[bold red]OpenAI Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")

if __name__ == "__main__":
    analyze_image()
