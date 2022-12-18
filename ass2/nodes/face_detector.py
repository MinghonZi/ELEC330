#!/usr/bin/env python

import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import torch
import rospy
import cv2
from rospkg import RosPack
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL import Image as Im


class FaceDetector:

    def __init__(self) -> None:
        self._model = torch.hub.load('ultralytics/yolov5', 'custom', Path(RosPack().get_path('ass2'))/'weights'/'yolov5l-face.pt')
        self._detector = rospy.Subscriber('/image_raw', Image, self._detect)
        self._detection_img = rospy.Publisher('/face_detection', Image, queue_size=1)
        self._bridge = CvBridge()

    def _detect(self, msg: Image) -> None:
        img = self._bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        detections = self._model(img)
        bounding_boxes = deepcopy(detections); bounding_boxes.render()
        detection_img = cv2.cvtColor(bounding_boxes.ims[0], cv2.COLOR_BGR2RGB)
        self._detection_img.publish(self._bridge.cv2_to_imgmsg(detection_img, "bgr8"))
        for crop in detections.crop(save=False):
            if re.search('^face', crop['label']):
                fp = Path('').resolve()/'face_snapshots'/f'{datetime.now().strftime("%Y%m%d%H%M%S%f")}.jpg'  # Path('') resolves to ~/.ros
                fp.parent.mkdir(parents=True, exist_ok=True)
                Im.fromarray(crop['im'][..., ::-1]).save(fp, quality=95, subsampling=0)


def process() -> None:
    rospy.init_node('face_detector')
    face_detector = FaceDetector()
    rospy.spin()


if __name__ == '__main__':
    try:
        process()
    except rospy.ROSInterruptException:
        pass
