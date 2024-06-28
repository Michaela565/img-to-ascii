import cv2 as cv

def main():
    img = cv.imread("kuromi.jpg", cv.IMREAD_GRAYSCALE)
    resize_img = cv.resize(img, (200, 200))
    cv.imshow("picture", resize_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()