# Perplexity AI Chat Assistant

A simple Python command-line chat assistant that leverages Perplexity AI's API to provide intelligent responses. This script demonstrates how to integrate with Perplexity's "sonar-pro" model using the OpenAI client library, maintaining conversation context throughout the interaction.

## Features

- **Interactive CLI Interface**: Simple command-line chat experience
- **Conversation Memory**: Maintains chat history for context-aware responses
- **Perplexity AI Integration**: Uses the powerful "sonar-pro" model
- **Easy Setup**: Minimal configuration required

## Prerequisites

- Python 3.6 or higher
- Perplexity AI API key
- Internet connection

## Installation

1. **Clone the repository**:
  
   git clone https://github.com/yourusername/perplexity-chat-assistant.git
   cd perplexity-chat-assistant


2. **Install dependencies**:
 
   pip install openai
  

3. **Configure API Key**:
   Replace the placeholder in the script:
   ```python
   key = "your_actual_api_key_here"
   ```
   
   > **Security Note**: For production use, consider using environment variables:
   > ```python
   > key = os.getenv('PERPLEXITY_API_KEY')
   > ```

## Usage

Run the script from your terminal:


python chat_assistant.py

The assistant will greet you and wait for your input:

```
Hi I am Your Assistant, How may I help you?
> What is artificial intelligence?
Assistant: [AI response here]
```

### Example Interaction

```
Hi I am Your Assistant, How may I help you?
> Explain quantum computing in simple terms
Assistant: Quantum computing is a revolutionary computing technology that uses quantum mechanical phenomena...
```

## Code Structure

```python
# Core components:
- OpenAI client initialization with Perplexity base URL
- Global messages list for conversation history
- completion() function for API interaction
- Main execution flow with user input handling
```

### Key Functions

- **`completion(message)`**: Handles API requests and response processing
- **Message Management**: Automatically maintains conversation context
- **Response Display**: Prints assistant responses and full conversation history

## Configuration Options

- **Model**: Currently uses "sonar-pro" (can be changed to other Perplexity models)
- **Base URL**: Configured for Perplexity AI API endpoint
- **Message History**: Automatically preserved for context

## API Key Setup

1. Sign up at [Perplexity AI](https://www.perplexity.ai/)
2. Navigate to your API dashboard
3. Generate a new API key
4. Replace the placeholder in the script

## Limitations

- **Single Turn**: Currently handles one question per session
- **No Error Handling**: Basic implementation without comprehensive error management
- **Hardcoded API Key**: Security consideration for production deployment

## Potential Enhancements

- Add loop for multi-turn conversations
- Implement error handling and retry logic
- Add command-line arguments for model selection
- Environment variable support for API key
- Conversation export functionality
- Custom system prompts

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Perplexity AI](https://www.perplexity.ai/) API
- Uses the OpenAI Python client library
- Inspired by the need for simple AI integration examples

## Support

If you encounter issues or have questions:
- Check the [Perplexity API Documentation](https://docs.perplexity.ai/)
- Open an issue on this repository
- Ensure your API key is valid and has sufficient credits

---

**Author**: Siddharth Sanjai  
**Purpose**: Learning and exploring AI technology integration
