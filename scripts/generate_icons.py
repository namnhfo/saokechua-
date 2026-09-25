import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('public/icons', exist_ok=True)

def create_app_icon(size, filename):
    # Tạo ảnh với nền gradient xanh ngọc hiện đại (Emerald)
    img = Image.new('RGBA', (size, size), (16, 185, 129, 255)) # Emerald 500
    draw = ImageDraw.Draw(img)
    
    # Tạo gradient hình chữ nhật bo tròn hoặc gradient nền
    margin = int(size * 0.08)
    corner_radius = int(size * 0.22)
    
    # Vẽ nền bo góc đẹp
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=corner_radius,
        fill=(5, 150, 105, 255), # Emerald 600
        outline=(52, 211, 153, 255), # Emerald 400
        width=int(size * 0.02)
    )

    # Vẽ biểu tượng đồng xu / ví tiền đơn giản và sắc nét
    center_x = size // 2
    center_y = size // 2
    
    # Đồng xu vòng ngoài
    coin_radius = int(size * 0.26)
    draw.ellipse(
        [(center_x - coin_radius, center_y - coin_radius),
         (center_x + coin_radius, center_y + coin_radius)],
        fill=(255, 255, 255, 240),
        outline=(209, 250, 229, 255),
        width=int(size * 0.03)
    )
    
    # Ký hiệu đồng tiền ở giữa (ký hiệu tiền tệ / chữ đ hoặc $)
    inner_radius = int(size * 0.18)
    draw.ellipse(
        [(center_x - inner_radius, center_y - inner_radius),
         (center_x + inner_radius, center_y + inner_radius)],
        outline=(16, 185, 129, 255),
        width=int(size * 0.02)
    )
    
    # Thanh ngang biểu thị sao kê / tăng trưởng
    bar_width = int(size * 0.06)
    draw.rounded_rectangle(
        [(center_x - int(size * 0.1), center_y - int(size * 0.02)),
         (center_x + int(size * 0.1), center_y + int(size * 0.04))],
        radius=int(bar_width / 2),
        fill=(5, 150, 105, 255)
    )

    img.save(filename, 'PNG')
    print(f"Generated {filename} ({size}x{size})")

create_app_icon(192, 'public/icons/icon-192x192.png')
create_app_icon(512, 'public/icons/icon-512x512.png')
create_app_icon(180, 'public/icons/apple-touch-icon.png')
create_app_icon(180, 'public/apple-touch-icon.png')
create_app_icon(192, 'public/icon-192.png')
create_app_icon(512, 'public/icon-512.png')
