from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import matplotlib.pyplot as plt
from PIL import Image
from colorthief import ColorThief
import colorsys


app = Flask(__name__)
bootstrap = Bootstrap5(app)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        image = request.files['image']
        image.save('C:/Users/chine/PycharmProjects/Image-color-palette-generator/static/assets/image.jpg')
        image_path = url_for('static', filename='assets/image.jpg')
        path = 'C:/Users/chine/PycharmProjects/Image-color-palette-generator/static/assets/image.jpg'

        pic = Image.open(path, mode="r").convert("RGBA")
        ct = ColorThief(image)
        colors = ct.get_color()
        # print(colors)
        # plt.imshow([colors])
        # plt.show()
        palette = ct.get_palette(color_count=10)
        print(palette)
        hexcode = []
        for color in palette:
            hex = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
            hexcode.append(hex)
        print(hexcode)
        plt.imshow([palette[i] for i in range(len(palette))])
        plt.show()
        return render_template('home.html', image_path=image_path, hexcode=hexcode)
    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True, port=5002)

