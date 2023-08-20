# Voice-powered Assistant by Nextech-Nexus

## Introduction

Welcome to the Voice-powered Assistant, a cutting-edge project by Nextech-Nexus! Our mission is to transform the way you interact with your emails and schedules. Through natural conversation, our assistant empowers you to efficiently manage meetings, compose emails, and derive valuable insights from your inbox.

## Features

- **Voice-activated Scheduling**: Set up meetings seamlessly.
- **Compose Emails**: Dictate your emails and have them ready to send.
- **Inbox Insights**: Gain quick insights from your emails, know what requires urgent attention.
- **Natural Language Processing**: Understands and processes user commands with high accuracy.

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nextech-Nexus/voice-powered-assistant.git

2. **Navigate to the Project Directory**:
   ```bash
   cd voice-powered-assistant

3. **Install Dependencies**:
   Make sure you have `pip` installed. Then, use the following command to install the necessary dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

4. **Setup Environment Variables**:
- Rename `.env.sample` to `.env`.
- Fill in the necessary environment variables.

5. **Run the Application**:
Detailed instructions can be found within the `streamlit_app` folder.

## Usage

Activate the Voice-powered Assistant by: 
- **pressing RECORD 3 times** (regretfully our team was filled with streamlit n00bs)
- Now give your voice command
- After you're done with your command press **STOP 1 time** ! 
- Now you will see "Running" on the top left corner (this means the bot is transcribing your voice command to text. Be patient!)
- When the agent is done it will output your voice command (in sound and written language)
- By **pressing STOP 2 more times** you'll be back where you started

A few examples:
- **Press RECORD 3 times** -> "Schedule a meeting with John tomorrow at 3 PM." ->  **Press STOP 1 time** -> Wait -> After answer **press STOP 2 more times** (and go again :))
- **Press RECORD 3 times** "Compose an email to [recipient@email.com] with the subject 'Project Update'." ->  **Press STOP 1 time** -> Wait -> After answer **press STOP 2 more times** (and go again :))
- **Press RECORD 3 times** "Show me unread emails from last week." ->  **Press STOP 1 time** -> Wait -> After answer **press STOP 2 more times** (and go again :))

## Note on FFmpeg

FFmpeg is essential for our voice assistant's sound output. Ensure you have it installed to prevent potential errors. 

> ❗ If you encounter any issues related to sound output, it's likely due to FFmpeg. 

To resolve this:
1. Visit [FFmpeg's official website](https://ffmpeg.org/).
2. Download the source code.
3. Remember to add FFmpeg to your system's PATH after installation.

## Contribution

We welcome contributions! Please follow the typical Git workflow:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request and we'll review as soon as possible.

## License

This project is licensed under the MIT License. See `LICENSE` for more details (if provided in the repo).

## Acknowledgements

- Big shoutout to the entire Nextech-Nexus team for their hard work and dedication.
- Special thanks to the open-source community for providing valuable tools and resources.
