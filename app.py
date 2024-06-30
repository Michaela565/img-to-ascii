import cv2 as cv

# TODO saving to a txt file

def main():
    img_path = input("What's the path to your image? ")
    should_file = input("Do you want to save the ASCII art to a file? yes = y, no = any character: ")
    file_name = ""
    if should_file == "y":
        file_name = input("Input the name of the file (If you input the name of an existing file, the data will be overwritten):")
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    file = open(file_name + ".txt", "w")
    width = 100
    height = 100
    resize_img = cv.resize(img, (width, height))
    char_bank = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "[", "]", ":", "{", "}", ";", "'", "|", ",", "<", ">", "?", "/", "~"]
    for row in range(width):
        pixel_count = 0 # Var to check if we are at the end of the row
        for col in range(height):
            pixel = resize_img[row, col]
            char_select = pixel // 10 # Selects which character from the char_bank to use
            if file_name != "":
                if pixel_count == width-1:
                    file.write(char_bank[char_select])
                    file.write("\n")
                else:
                    file.write(char_bank[char_select])
            if pixel_count == width-1:
                print(char_bank[char_select])
            else:
                print(char_bank[char_select], end=" ")
            pixel_count += 1
    file.close()
if __name__ == "__main__":
    main()