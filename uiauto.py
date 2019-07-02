from uiautomator import device as d
from uiautomator import Device

sn1 = "STS0119301000456"
d = Device(sn1)
# d.sleep()
d(text="时钟").click()

