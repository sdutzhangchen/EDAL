from Networks.VGG16.teacher import decoder as vgg
from Networks.VGG16.VGG0_5 import decoder as vgg_source
from Networks.VGG16.teacher import TeacherModel as vgg_teacher
from Networks.VGG16.KD import Model as kd_EADA
from Networks.HR_Net.seg_hrnet import get_seg_model as hrnet
from Networks.VGG.VGG19 import Vgg19_net as VGG19
from Networks.OSNet.os import decoder as os
model_dict = {
    "vgg":vgg,
    "kd_EADA":kd_EADA,
    "vgg_teacher":vgg_teacher,
    "vgg_source":vgg_source,
    "hrnet":hrnet,
    "VGG19":VGG19,
    "os":os,
}