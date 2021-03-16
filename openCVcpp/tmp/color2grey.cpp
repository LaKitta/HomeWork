#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace std;

int main() {
    string img_path = "media/cat.jpg";

    cv::Mat cat = cv::imread(img_path, cv::IMREAD_COLOR);

    if (cat.empty()) {
        cout << "Could not load image" << endl;
        return 1;
    }

    cv::rotate(cat, cat, cv::ROTATE_180);
    cv::resize(cat, cat, cv::Size(500, 500));

    for (int i = 0; i < cat.rows; i++) {
        for (int t = 0; t < cat.cols;t++) {
            cv::Vec3b bgrPixel = cat.at<cv::Vec3b>(i, t);
            // cout << "bgr:" << bgrPixel << endl;
            unsigned char grayScale = (bgrPixel[0] + bgrPixel[1] + bgrPixel[2]) / 3;
            cat.at<cv::Vec3b>(i, t) = { grayScale, grayScale, grayScale };
            cv::Vec3b grayPixel = cat.at < cv::Vec3b>(i, t);
            // cout << "gray:" << grayPixel << endl;
        }
    }

    cv::imshow("Grayed", cat);
    int k = cv::waitKey(0);
    if (k == 's') {
        cv::imwrite("what is what", cat);
    }
    return 0;
}

