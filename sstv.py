import numpy as np
from scipy.io import wavfile
from Pillow import Image

def decode_pd120(wav_file, output_image):
    # Load the audio file
    sample_rate, data = wavfile.read(wav_file)
    
    # Determine image dimensions
    width = 640
    height = len(data) // (width * 2)  # Each row consists of two samples

    # Reshape audio data into image format
    image_data = np.reshape(data, (height, width * 2))

    # Normalize image data
    image_data = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data)) * 255

    # Convert image data to uint8
    image_data = image_data.astype(np.uint8)

    # Create image
    img = Image.fromarray(image_data)

    # Save image
    img.save(output_image)

    print(f"Image saved as {output_image}")

if __name__ == "__main__":
    # Example usage
    decode_pd120("pd120_audio.wav", "decoded_image.png")
