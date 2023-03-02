# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import argparse
import os
import time
from loguru import logger

import cv2

import torch

from yolox.data.data_augment import ValTransform
from yolox.data.datasets import COCO_CLASSES
from yolox.data.datasets import voc_classes

from yolox.exp import get_exp
from yolox.utils import fuse_model, get_model_info, postprocess, vis
from configs.config import conf_thres, nms_thres, img_size, config_path, weight_path


class Predictor(object):
    def __init__(
            self,
            model,
            exp,
            cls_names=voc_classes,
            decoder=None,
            device="gpu",
            fp16=False,
            legacy=False,
    ):
        self.model = model
        self.cls_names = cls_names
        self.decoder = decoder
        self.num_classes = exp.num_classes
        self.confthre = exp.test_conf
        self.nmsthre = exp.nmsthre
        self.test_size = exp.test_size
        self.device = device
        self.fp16 = fp16
        self.preproc = ValTransform(legacy=legacy)

    def inference(self, img):
        img_info = {"id": 0}
        if isinstance(img, str):
            img_info["file_name"] = os.path.basename(img)
            img = cv2.imread(img)
        else:
            img_info["file_name"] = None

        height, width = img.shape[:2]
        img_info["height"] = height
        img_info["width"] = width
        img_info["raw_img"] = img

        ratio = min(self.test_size[0] / img.shape[0], self.test_size[1] / img.shape[1])
        img_info["ratio"] = ratio

        img, _ = self.preproc(img, None, self.test_size)
        img = torch.from_numpy(img).unsqueeze(0)
        img = img.float()
        if self.device == "gpu":
            img = img.cuda()
            if self.fp16:
                img = img.half()  # to FP16

        with torch.no_grad():
            t0 = time.time()
            outputs = self.model(img)
            if self.decoder is not None:
                outputs = self.decoder(outputs, dtype=outputs.type())
            outputs = postprocess(
                outputs, self.num_classes, self.confthre,
                self.nmsthre, class_agnostic=True
            )
            # logger.info("Infer time: {:.4f}s".format(time.time() - t0))
        return outputs, img_info

    def visual(self, output, img_info, cls_conf=0.35):
        ratio = img_info["ratio"]
        img = img_info["raw_img"]
        if output is None:
            return img
        output = output.cpu()

        bboxes = output[:, 0:4]

        # preprocessing: resize
        bboxes /= ratio

        cls = output[:, 6]
        scores = output[:, 4] * output[:, 5]

        vis_res = vis(img, bboxes, scores, cls, cls_conf, self.cls_names)
        return vis_res


def set_model(conf, nms, tsize):

    exp = get_exp(config_path)
    exp.test_conf = conf
    exp.nmsthre = nms
    exp.test_size = (tsize, tsize)

    model = exp.get_model()
    model.cuda()
    model.eval()
    logger.info("loading checkpoint")
    ckpt = torch.load(weight_path, map_location="cpu")
    # load the model state dict
    model.load_state_dict(ckpt["model"])

    predictor = Predictor(model, exp, voc_classes)
    return predictor


def imageflow_demo(predictor):
    # cap = cv2.VideoCapture(args.path if args.demo == "video" else args.camid)
    cap = cv2.VideoCapture("rtsp://admin:hdu417417@192.168.2.6/Streaming/Channels/101")
    while True:
        ret_val, frame = cap.read()
        if ret_val:
            frame = cv2.resize(frame, (1920, 1080))
            outputs, img_info = predictor.inference(frame)
            result_frame = predictor.visual(outputs[0], img_info, predictor.confthre)
            result_frame = cv2.resize(result_frame, (640, 480))
            cv2.imshow("123", result_frame)
            ch = cv2.waitKey(1)
            if ch == 27 or ch == ord("q") or ch == ord("Q"):
                break
        else:
            break


if __name__ == '__main__':
    model = set_model(conf_thres, nms_thres, img_size)
    imageflow_demo(model)
