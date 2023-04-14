# Hash Fingerprint Image Generator
![alt text](https://github.com/finnfassnacht/hash-fingerprint-image/blob/main/example.png)

The Hash Fingerprint Image Generator is a Python script that generates images based on SHA-256 hashes, allowing users to fingerprint their data. The script uses the PIL library to generate images that are 400x400 pixels in size. The script can take files, words, and hashes, and then creates an image based on the hash or data.

## Installation
First install the required libraries by running the following command in the terminal:
```
pip3 install pillow
```
Then, clone this repository using the following command:
```
git clone https://github.com/finnfassnacht/hash-fingerprint-image.git
```
Then navigate to the cloned directory:
```
cd hash-fingerprint-image
```
## Usage

You can use the script to generate an image based on a file, a word, or a hash.

To generate an image based on a file, use the following command:
```
python3 fingerprint.py --file file_path image_file_name.jpg
```
To generate an image based on a word, use the following command:
```
python3 fingerprint.py --data "your word" image_file_name.jpg
```
To generate an image based on a hash, use the following command:
```
python3 fingerprint.py --hash "your hash" image_file_name.jpg
```
Replace "your hash" with the SHA-256 hash you want to use and image_file_name.jpg with the name of the output image file you want to use.

The script supports the following image file types: JPG, JPEG, PDF, and PNG, as well as any other file types supported by the PIL library.

## How it works

When you provide a file or word to the script, it first generates a SHA-256 hash of the input data. The script then splits the 64-length hash into 16 strings, each of which is 4 characters long. These fragments are converted to a list of numbers, with the squares' colors being an RGB value from the first three numbers in the list. The last number in the list defines the width of the square. This process is repeated 16 times to fingerprint the entire 64-character hash. The resulting image contains 16 squares arranged in a 4x4 pattern.
