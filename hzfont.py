from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

def render_text_to_image(font_path, text, font_size):  
    image_size=(font_size,font_size)    #画布大小 保持一致即可
    font = TTFont(font_path)
    ttf = font['cmap'].tables[0]
    image = Image.new("RGBA", image_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    try:
        pil_font = ImageFont.truetype(font_path, font_size)
    except:
        pil_font = ImageFont.load_default()
    draw.text((0, 0), text, font=pil_font, fill=(255, 255, 255, 255))   #字体基于画布位置 个别字体微调
    return image

def extract_alpha_from_image(image):
    alpha_channel = image.split()[3]
    width, height = image.size
    
    alpha_hex_values = []
    
    for y in range(height):
        for x in range(width):
            alpha = alpha_channel.getpixel((x, y))
            alpha_hex = f"0x{alpha:02x}"    # 转为十六进制，并添加 "0x" 前缀
            alpha_hex_values.append(alpha_hex)
    
    return alpha_hex_values

font_path = "C:/Users/24994/Desktop/simhei.ttf" #加载源字体
font_str = "提示标题"   #要转换的汉字
text_to_render = "1"
size = 16   #字体大小
print("const unsigned char HZfont[]={")
for index in range(len(font_str)):
    print("/"+font_str[index]+"*/")
    text_to_render = font_str[index]
    rendered_image = render_text_to_image(font_path, text_to_render,size)
    alpha_hex_values = extract_alpha_from_image(rendered_image)
    if alpha_hex_values:
        result = ", ".join(alpha_hex_values)
        print("", result)
        print(",")
        # print("总像素数:", len(alpha_hex_values))
print("};")