import PIL.Image

ascii_values = ["$", "@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", "'"]


# Resizes image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# Converts the image to grey
def grayscaler(image):
    return image.convert("L")


# Convert pixels in to ascii characters
def pixel_ascii_converter(image):
    pixels = image.getdata()
    characters = "".join([ascii_values[pixel // 23] for pixel in pixels])
    return characters


def main(new_width=100):
    while True:  # Loop to keep asking for the file path until a valid one is provided
        path = input("Please enter path to the desired image or type 'quit' to exit: ")
        if path.lower() == "quit":  # Check if user wants to quit
            print("Exiting the program.")
            return  # Exit the function

        try:
            image = PIL.Image.open(path)
            break  # Break the loop if the image is successfully opened
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    new_image_data = pixel_ascii_converter(grayscaler(resize_image(image, new_width)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i : (i + new_width)] for i in range(0, pixel_count, new_width)
    )

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()
