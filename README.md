# Image-to-HTML Generator

This Python application utilizes OpenAI's powerful GPT model to analyze images and generate corresponding HTML code that attempts to visually replicate the content and structure seen in the image. This tool is particularly useful for web developers looking to convert static images into interactive HTML templates.

## Features

- **Image Analysis:** Leverages OpenAI's GPT-4-1106-vision-preview model to interpret the visual content of an image.
- **HTML Generation:** Generates detailed HTML/CSS based on the analysis to closely match the design shown in the image.
- **Iterative Refinement:** Processes the image description through multiple iterations to enhance the accuracy of the output.
- **Progress Tracking:** Uses `tqdm` to show progress during the generation process.

## Prerequisites

Before you start using this application, ensure you have the following installed:
- Python 3.7+
- `openai` Python library
- `click`, `rich`, `tqdm` libraries

You also need to have an OpenAI API key configured as an environment variable (`OPENAI_API_KEY`).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rjslvn/img2html.git

   ```

## Usage

To run the application, execute the following command in your terminal:

```bash
python app.py
```

You will be prompted to enter the URL of the image you want to analyze. After entering the URL, the application will begin processing and will output the generated HTML in the terminal as well as save it to a file named `final_output.html`.

## Configuration

No additional configuration is needed beyond setting up the `OPENAI_API_KEY` environment variable.

## Contributing

Contributions to enhance the functionality, improve the HTML/CSS generation accuracy, or refine the user interface are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, contact [your-email@example.com] or open an issue in the GitHub repository.

## Acknowledgements

- Thanks to OpenAI for providing the API that powers this tool.
- Thanks to the developers of `click`, `rich`, and `tqdm` for their fantastic Python libraries that enhance this application's functionality.
