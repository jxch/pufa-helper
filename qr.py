import qrcode

# 创建一个二维码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据
qr.add_data('http://8.142.100.222:5100/deaf_guide')
qr.make(fit=True)

# 创建一个图像对象
img = qr.make_image(fill='black', back_color='white')

# 保存图像
img.save('qrcode.png')
