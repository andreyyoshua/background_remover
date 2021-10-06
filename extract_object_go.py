import pixellib
from pixellib.tune_bg import alter_bg

unix = sys.argv[1]
files = glob.glob("/Users/ferico/go/src/go-image/img/*"+unix+"*")

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

for file in files:
    change_bg.color_bg(file, colors = (255, 255, 255), output_image_name="./output/" + file)
