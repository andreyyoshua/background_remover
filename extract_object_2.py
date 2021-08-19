import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

for i in range(1, 61):
    change_bg.color_bg("./nuvo/" + str(i) + ".jpeg", colors = (255, 255, 255), output_image_name="./output/" + str(i) + "colored_bg.jpg")
