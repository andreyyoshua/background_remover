import pixellib
from pixellib.instance import instance_segmentation


segment_video = instance_segmentation()
segment_video.load_model("mask_rcnn_coco.h5")
target_classes = segment_video.select_target_classes(person=True)
segment_video.process_video("perfume.MOV", show_bboxes=True, segment_target_classes= target_classes, extract_segmented_objects=True,
save_extracted_objects=True, frames_per_second= 5,  output_video_name="output.mp4")