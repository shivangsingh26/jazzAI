# jazzAI

jazzAI is a Python-based music generation application leveraging the `facebook/musicgen-melody` model from Hugging Face and MetaAI's Audiocraft library. It offers a user-friendly interface built with Streamlit, allowing users to input a MIDI file and select a duration for generating music. The application enables users to listen to and download the generated music directly. Additionally, a package check feature is included to ensure smooth operation.

## Features

- **Music Generation**: Generate music from MIDI files using advanced models.
- **User Interface**: Simple and intuitive interface built with Streamlit.
- **Downloadable Output**: Generated music can be listened to and downloaded.
- **Package Check**: Ensures all necessary packages are installed for seamless operation.

## Installation

To get started with jazzAI, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ssnfs26/jazzAI.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd jazzAI
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Generate Music**:
    - Enter the type of music you want to generate.
    - Select the desired duration for music generation.
    - Listen to the generated music and download it directly from the application.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.
