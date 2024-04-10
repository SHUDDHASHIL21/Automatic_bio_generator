# Automatic Bio Generator

Automatically generate captivating bios with ease! This project provides a web application built with Flask, capable of generating multiple unique biographies based on user-provided inputs. Whether you're looking to spruce up your social media profiles, create a compelling dating bio, or enhance your professional online presence, the Automatic Bio Generator has you covered.

## Features

- **Easy to Use**: Simply provide your name, gender, marital status, interests, profession, and religion, and let the generator do the rest.
- **Unique Biographies**: Receive five unique and engaging biographies tailored to your input, ensuring diversity and personalization.
- **Customizable Templates**: The application includes a variety of pre-defined bio templates, which are randomized to offer different narrative styles.
- **Error Handling**: Robust error handling ensures smooth operation, with informative messages provided in case of any issues.
- **Open Source**: Feel free to explore, modify, and contribute to the project's codebase. It's hosted on GitHub under an open-source license.

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/automatic-bio-generator.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python bio_gen_app.py`
4. Access the application in your web browser at `http://localhost:5000`

## Usage

1. Make a POST request to the `/generate_bio` endpoint with JSON data containing your desired inputs (name, gender, marital status, interests, profession, and religion).
2. Receive a JSON response containing five unique biographies tailored to your input.


### Sample Input JSON : 
{
  "name": "John Doe",
  "gender": "Male",
  "marital_status": "Single",
  "interests": "Traveling, Photography",
  "profession": "Software Engineer",
  "religion": "None"
}

## Contributing

Contributions are welcome! Whether you'd like to add new features, improve existing functionality, or fix bugs, feel free to fork the repository, make your changes, and submit a pull request.
