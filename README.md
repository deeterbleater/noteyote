# NoteYote

Welcome to NoteYote, an integrated Jupyter notebook and ChatGPT application designed to enhance your productivity and streamline your workflow.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

NoteYote combines the power of Jupyter notebooks with the conversational capabilities of ChatGPT. This application allows users to interact with Jupyter notebooks and receive AI assistance from ChatGPT, all within a unified interface.

## Features

- **Jupyter Integration**: Seamlessly interact with Jupyter notebooks.
- **ChatGPT Assistance**: Get help, suggestions, and code completions from ChatGPT.
- **Split View**: View and interact with Jupyter notebooks and ChatGPT side by side.
- **Task Management**: Manage your tasks efficiently within the application.
- **Real-time Collaboration**: Collaborate with team members in real-time.

## Installation

### Prerequisites

- Python 3.8 or higher
- Node.js and npm

### Backend (FastAPI)

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/noteyote.git
    cd noteyote
    ```

2. Set up a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

### Frontend (SvelteKit)

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Start the SvelteKit development server:
    ```sh
    npm run dev
    ```

### Environment Variables

Create a `config.ini` file in the root directory and add the following variables:
[KEY]
OPENAI_API_KEY=your-api-key



## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using NoteYote! If you have any questions or feedback, feel free to open an issue or reach out to us.


