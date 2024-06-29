import cv2 as cv

def main():
    img_path = "kuromi.jpg"
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    width = 100
    height = 100
    resize_img = cv.resize(img, (width, height))
    character_bank = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "[", "]", ":", "{", "}", ";", "'", "|", ",", "<", ">", "?", "/", "~"]
    for row in range(width):
        pixel_count = 0 # Var to check if we are at the end of the row
        for col in range(height):
            pixel = resize_img[row, col]
            # print(pixel//10)
            character_select = pixel // 10
            if pixel_count == width-1:
                print(character_bank[character_select])
            else:
                print(character_bank[character_select], end=" ")
            pixel_count += 1
            


    cv.imshow("picture", resize_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()