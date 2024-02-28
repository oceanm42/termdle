# Termdle

Termdle is a simple word-guessing game played in the terminal. The objective is to guess a secret word within a limited number of attempts. This project is inspired by the popular game "Wordle."

## Features

- Interactive gameplay in the terminal.
- Randomly selects a word from a provided word list.
- Keeps track of previous guesses.
- Visual feedback on correct and incorrect guesses.
- Supports resetting the game and quitting at any time.

## Usage

Clone repository
```bash
git clone https://github.com/oceanm42/termdle.git
cd termdle
```

Install requirements
```bash
pip install requirements.txt
```

Create a word list file (`example_word_list.txt`) containing a list of words, one word per line.

Example
```python
from termdle import Termdle

termdle = Termdle("example_word_list.txt").start()
```

## Contributing

Contributions are welcome! If you have suggestions or found a bug, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
