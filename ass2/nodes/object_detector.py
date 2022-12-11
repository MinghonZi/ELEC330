#!/usr/bin/env python

import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import torch
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL import Image as Im


class ObjectDetector:

    def __init__(self) -> None:
        self._model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)  # https://github.com/ultralytics/yolov5/issues/36
        self._detector = rospy.Subscriber('/manmaru/camera_front/image_raw', Image, self._detect)
        self._detection_img = rospy.Publisher('/object_detection', Image, queue_size=1)
        self._bridge = CvBridge()

    def _detect(self, msg: Image):
        img = self._bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        detections = self._model(img)
        bounding_boxes = deepcopy(detections); bounding_boxes.render()  # https://stackoverflow.com/a/73883234/20015297
        detection_img = cv2.cvtColor(bounding_boxes.ims[0], cv2.COLOR_BGR2RGB)  # Because of OpenCV reading images as BGR
        self._detection_img.publish(self._bridge.cv2_to_imgmsg(detection_img, "bgr8"))
        return detections


class PersonSnapshooter(ObjectDetector):

    def __init__(self) -> None:
        super().__init__()

    # @override
    def _detect(self, msg: Image) -> None:
        """
        Detect class 'person' and save the cropped image in ~/.ros/person_snapshots/

        Based on the original code:
        - https://github.com/ultralytics/yolov5/blob/342fe05e6c88221750ce7e90b7d2e8baabd397dc/models/common.py#L754
        - https://github.com/ultralytics/yolov5/blob/342fe05e6c88221750ce7e90b7d2e8baabd397dc/utils/plots.py#L544
        """
        detections = super()._detect(msg)
        for crop in detections.crop(save=False):
            if re.search('^person', crop['label']):
                fp = Path('').resolve()/'person_snapshots'/f'{datetime.now().strftime("%Y%m%d%H%M%S%f")}.jpg'  # Path('') resolves to ~/.ros
                fp.parent.mkdir(parents=True, exist_ok=True)
                Im.fromarray(crop['im'][..., ::-1]).save(fp, quality=95, subsampling=0)


def process() -> None:
    rospy.init_node('object_detector')
    person_snapshooter = PersonSnapshooter()
    rospy.spin()


if __name__ == '__main__':
    try:
        process()
    except rospy.ROSInterruptException:
        pass
