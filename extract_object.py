import pixellib

from pixellib.instance import instance_segmentation

segment_image=instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")
target_classes = segment_image.select_target_classes()
segment_image.segmentImage("image_1.jpg", 
extract_segmented_objects=True,
save_extracted_objects=True, 
segment_target_classes=target_classes,
show_bboxes=True,  
output_image_name="output.jpg")