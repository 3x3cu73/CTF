import numpy as np
from PIL import Image

def extract_lsb_data(image_path):
    """
    Extract least significant bit data from a PNG image and convert to ASCII.
    
    Args:
        image_path (str): Path to the PNG image
        
    Returns:
        str: The extracted ASCII message
    """
    # Open the image
    img = Image.open(image_path)
    # Convert to NumPy array
    img_array = np.array(img)
    
    # Get image dimensions
    height, width, channels = img_array.shape
    
    # Initialize variables to store binary data
    binary_data = ""
    
    # Extract the LSB from each pixel
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                # Extract the least significant bit
                binary_data += str(img_array[h, w, c] & 1)
    
    # Convert binary string to ASCII characters
    ascii_data = ""
    # Process in groups of 8 bits (1 byte)
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:  # Make sure we have a full byte
            # Convert byte to decimal and then to ASCII
            decimal_value = int(byte, 2)
            # Check for null terminator or non-printable characters
            if decimal_value == 0:
                break  # End of message (null terminator)
            if decimal_value >= 32 and decimal_value <= 126:  # Printable ASCII range
                ascii_data += chr(decimal_value)
    
    return ascii_data

def main():
    image_path = input("Enter the path to the PNG image: ")
    try:
        extracted_text = extract_lsb_data(image_path)
        print("\nExtracted ASCII message:")
        print(extracted_text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
