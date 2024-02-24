# Cipher

Cipher is a simple yet powerful web application that provides encryption and decryption services. It's available at [cipher.andresousa.pt](https://cipher.andresousa.pt).

## Motivation

In the digital age, the security of sensitive information is paramount. We often rely on various online services to handle our data, but the question remains - are these services truly secure? Can we trust them not to store our secret data?

Cipher was born out of these concerns. It's not just another service; it's a commitment to data privacy and security. Cipher provides a platform where users can encrypt and decrypt their sensitive information without the worry of their data being stored.

With Cipher, your data is yours and yours alone. We don't store it; we just help you protect it. It's a simple solution for a complex problem, aiming to foster a safer digital environment where privacy is not just a promise, but a practice.


## Contributing

We welcome contributions from everyone. If you're interested in contributing:

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## Issues

If you find any bugs or have a feature request, please open an issue on GitHub. We appreciate any and all feedback. Please be as detailed as possible in your issue description.

## Roadmap

Here are some improvements and new features we are considering:

- [ ] **Implement Continuous Integration**: We plan to set up a CI pipeline that automatically runs tests for each pull request. This will help ensure that all changes and additions to the codebase maintain the existing functionality and do not introduce new bugs. Status checks will be required to pass before merging.

- [ ] **Develop the Frontend**: We plan to design and implement a user-friendly and intuitive frontend for the application.

- [ ] **Add Support for Other Encryption Algorithms**: Currently, the application only supports AES encryption. We plan to add support for other popular encryption algorithms like DES or RSA.

- [ ] **User Accounts and Authentication**: We are considering adding user account functionality, which would allow users to save their encryption keys and encrypted data securely.

- [ ] **Rate Limiting**: To prevent abuse of the API, we plan to implement rate limiting.

- [ ] **Improved Error Handling**: We aim to improve our error handling to provide more informative error messages to the user.

Please note that these are just ideas and there is no guarantee when or if these features will be implemented. We welcome contributions and suggestions.
## API Usage

For power users who prefer to use the API directly instead of the web interface, the following endpoint is available:

### Encrypt

**POST:** `https://cipher-api.andresousa.pt/?action=encrypt`

**Request Body:**
```json
{
    "secret_key": "<your_secret_key>",
    "data": "<data_to_encrypt>"
}
```
**Response:**
```json
{
    "message": "<encrypted_data>"
}
```

Replace <your_secret_key> with your secret key and <data_to_encrypt> with the data you want to encrypt. 

The API will return the encrypted message in the message field of the response. 

Please note that the actual encrypted message will vary based on the secret key and data provided.

### Decrypt

**POST:** `https://cipher-api.andresousa.pt/?action=decrypt`

**Request Body**
```json
{
    "secret_key": "<your_secret_key>",
    "data": "<data_to_decrypt>"
}
```

**Response:**
```json
{
    "message": "<decrypted_data>"
}
```