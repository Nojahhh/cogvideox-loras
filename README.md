# CogVideoX-LoRAs

**CogVideoX-LoRAs** is a centralized repository for all LoRA (Low-Rank Adaptation) models created for **CogVideoX**. This project addresses the need for a unified platform to collect, share, and contribute to various LoRA models, making it easier for users, developers, and researchers to enhance their video generation workflows.

## Table of Contents
- [Features](#features)
- [LoRA Models](LORA_MODELS.md)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Comprehensive Collection**: A growing repository of all available LoRAs created for CogVideoX.
- **Community Contributions**: Open to contributions from the community, fostering collaboration in LoRA model development.
- **Easy Access**: Clear organization and categorization of LoRA models for easy discovery and usage.
- **Up-to-Date Listings**: Regularly updated with the latest LoRA models, ensuring this repository remains the go-to source for CogVideoX customizations.

## LoRA Models
For a detailed list of available LoRA models, please refer to the [LORA_MODELS.md](LORA_MODELS.md) file in the repository.

## Contributing
Contributions are welcome! If you would like to contribute to this repository, please follow these steps:
1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork** to your local machine:
  ```bash
  git clone https://github.com/your-username/cogvideox-loras.git
  ```

3. **Navigate to the Repository Directory**:
  ```bash
  cd cogvideox-loras
  ```

4. **Run the `add_new_lora.py` Script** to add a new LoRA model:
  ```bash
  python add_new_lora.py
  ```

  This script will fetch model data from Hugging Face and append it to the `LORA_MODELS.md` file.

5. **Commit Your Changes**:
  ```bash
  git add LORA_MODELS.md
  git commit -m "Added new LoRA to list"
  ```

6. **Push to Your Fork**:
  ```bash
  git push origin main
  ```

7. **Open a Pull Request** detailing your changes.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.

## Contact
For inquiries or feedback, please contact [mellin.johan@gmail.com].
