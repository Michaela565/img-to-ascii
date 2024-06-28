import cv2 as cv

def main():
    img = cv.imread("kuromi.jpg", cv.IMREAD_GRAYSCALE)
    width = 200
    height = 200
    resize_img = cv.resize(img, (200, 200))

    for row in range(height):
        for col in range(width):
            pixel = resize_img[row, col]
            print(pixel)


    cv.imshow("picture", resize_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()