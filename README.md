# Cipher

Cipher is a web application that provides encryption and decryption services. It has a frontend available at [cipher.andresousa.pt](https://cipher.andresousa.pt).


## Contributing

We welcome contributions from everyone. If you're interested in contributing:

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## Issues

If you find any bugs or have a feature request, please open an issue on GitHub. We appreciate any and all feedback. Please be as detailed as possible in your issue description.

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