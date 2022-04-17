import os
import argparse
import random

def gen_html(data_dirs, out_dir, scale):
  groups = [os.path.basename(o) for o in data_dirs]


  title = 'portrait retouching user study'


  lines = []
  lines.append('<!DOCTYPE html>') 
  lines.append('<html>')
  lines.append('<head>')
  lines.append('<title>%s</title>' % title)
  
  lines.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
  lines.append('<script src="FileSaver.js"></script>')
  lines.append('<style>')
  lines.append('* {box-sizing: border-box}')
  lines.append('body {font-family: Verdana, sans-serif; margin:0}')
  lines.append('.mySlides {display: none}')
  lines.append('img {vertical-align: middle;}')
  lines.append('.slideshow-container {')
  lines.append('  max-width: 1920px;')
  lines.append('  position: relative;')
  lines.append('  margin: auto;')
  lines.append('}')
  lines.append('.prev, .next {')
  lines.append('  cursor: pointer;')
  lines.append('  position: absolute;')
  lines.append('  top: 50%;')
  lines.append('  width: auto;')
  lines.append('  padding: -10px;')
  lines.append('  margin-top: -22px;')
  lines.append('  color: blue;')
  lines.append('  font-weight: bold;')
  lines.append('  font-size: 38px;')
  lines.append('  transition: 0.6s ease;')
  lines.append('  border-radius: 0 3px 3px 0;')
  lines.append('}')
  lines.append('.next {')
  lines.append('  right: 0;')
  lines.append('  border-radius: 3px 0 0 3px;')
  lines.append('}')
  lines.append('.prev:hover, .next:hover {')
  lines.append('  background-color: rgba(0,0,0,0);')
  lines.append('}')
  lines.append('.text {')
  lines.append('  text-align: center;')
  lines.append('}')

  lines.append('.numbertext {')
  lines.append('  color: #f2f2f2;')
  lines.append('  font-size: 12px;')
  lines.append('  padding: 8px 12px;')
  lines.append('  position: absolute;')
  lines.append('  top: 0;')
  lines.append('}')
  lines.append('.dot {')
  lines.append('  cursor: pointer;')
  lines.append('  height: 15px;')
  lines.append('  width: 15px;')
  lines.append('  margin: 0 2px;')
  lines.append('  background-color: #bbb;')
  lines.append('  border-radius: 5%;')
  lines.append('  display: inline-block;')
  lines.append('  transition: background-color 0.6s ease;')
  lines.append('}')
  lines.append('.active, .dot:hover {')
  lines.append('  background-color: #717171;')
  lines.append('}')
  lines.append('.fade {')
  lines.append('  -webkit-animation-name: fade;')
  lines.append('  -webkit-animation-duration: 1.5s;')
  lines.append('  animation-name: fade;')
  lines.append('  animation-duration: 1.5s;')
  lines.append('}')

  lines.append('@-webkit-keyframes fade {')
  lines.append('  from {opacity: .4} ')
  lines.append('  to {opacity: 1}')
  lines.append('}')

  lines.append('@keyframes fade {')
  lines.append('  from {opacity: .4} ')
  lines.append('  to {opacity: 1}')
  lines.append('}')
  lines.append('@media only screen and (max-width: 300px) {')
  lines.append('  .prev, .next,.text {font-size: 11px},')
  lines.append('   .column {')
  lines.append('        width: 100%;')
  lines.append('    }')
  lines.append('}')

  lines.append('.column {')
  lines.append('    float: left;')
  lines.append('    width: 32%;')
  lines.append('    padding: 5px;')
  lines.append('}')

  lines.append('.row::after {')
  lines.append('    content: "";')
  lines.append('    clear: both;')
  lines.append('    display: table;')
  lines.append('}')

  lines.append('#div_in {')
  lines.append('    float: left;')
  lines.append('    width: 480px;')
  lines.append('    height: 256px;')
  lines.append('    margin: 1px;')
  lines.append('    padding: 1px;')
  lines.append('    border: 1px dotted black;')
  lines.append('}')

  lines.append('.div {')
  lines.append('    float: left;')
  lines.append('    width: 480px;')
  lines.append('    height: 270px;')
  lines.append('    margin: 1px;')
  lines.append('    padding: 1px;')
  lines.append('    border: 1px solid black;')
  lines.append('}')
  lines.append('</style>')
  lines.append('</head>')

  lines.append('<body>')
  lines.append('<div class="slideshow-container">')

  # lines.append('<p>I\'m KD')
  # lines.append('   KD videos</p>')
  # lines.append('<p>Are you OK?</p>')

  data_dir = data_dirs[0]
  items = [o for o in os.listdir(data_dir)]

  items.sort()

  div_id=0

  for item in items:
    out_path = os.path.join(out_dir, 'index_{}.html'.format(item))
    print('save', out_path)
    fout = open(out_path, 'w')
    lines_out = lines.copy()
    print("item:", item)
    lines_out.append('<div class="mySlides fade">')
    lines_out.append('<div class="row">')
    dir_to_list = data_dir +'/' + item
    groups = [o for o in os.listdir(dir_to_list)]
    lines_out.append("<div class='article-title-box'> <h1 class='title-article' id='articleContentId'> group id: {} \n  </h1> </div>".format(item.split('subset_')[1]))
    divin_id = 0
    for g in groups:
      lines_out.append('<b>img id: {}\n</b>'.format(divin_id))
      print("g:", g)
      video_name = dir_to_list + '/' + g
      lines_out.append('<figure data-size="normal">')
      td2 = '<img src="{}">'.format(video_name)
      lines_out.append(td2)
      lines_out.append('</img>')
      lines_out.append('</figure>')
      # lines_out.append("<div class='text' aria-hidden='true'> -------1  ----------   2-------- </div>")
      divin_id += 1
      lines_out.append("<div class='article-title-box'> <h1 class='title-article' id='articleContentId'>          ----------------------1  ---------------------   2   -------- </h1> </div>")

      lines_out.append('</div>')
      lines_out.append('</div>')


    lines_out.append('</div>')

    lines_out.append('<br>')
    lines_out.append('<div style="text-align:center">')
    lines_out.append('  <span class="dot" onclick="currentSlide(1)"></span>')
    lines_out.append('  <span class="dot" onclick="currentSlide(2)"></span>')

    lines_out.append('</div>')


    lines_out.append('<script>')

    lines_out.append('var slideIndex = 1;')
    lines_out.append('showSlides(slideIndex);')

    lines_out.append('function plusSlides(n) {')
    lines_out.append('  showSlides(slideIndex += n);')
    lines_out.append('}')

    lines_out.append('function currentSlide(n) {')
    lines_out.append('  showSlides(slideIndex = n);')
    lines_out.append('}')

    lines_out.append('function showSlides(n) {')
    lines_out.append('  var i;')
    lines_out.append('  var slides = document.getElementsByClassName("mySlides");')
    lines_out.append('  var dots = document.getElementsByClassName("dot");')
    lines_out.append('  if (n > slides.length) {slideIndex = 1}    ')
    lines_out.append('  if (n < 1) {slideIndex = slides.length}')
    lines_out.append('  for (i = 0; i < slides.length; i++) {')
    lines_out.append('      slides[i].style.display = "none";  ')
    lines_out.append('  }')
    lines_out.append('  for (i = 0; i < dots.length; i++) {')
    lines_out.append('     dots[i].className = dots[i].className.replace(" active", "");')
    lines_out.append('  }')
    lines_out.append('  slides[slideIndex-1].style.display = "block";  ')
    lines_out.append('  dots[slideIndex-1].className += " active";')
    lines_out.append('}')

    lines_out.append('function allowDrop(ev) {')
    lines_out.append('    ev.preventDefault();')
    lines_out.append('}')

    lines_out.append('function drag(ev) {')
    lines_out.append('    ev.dataTransfer.setData("text", ev.target.id);')
    lines_out.append('}')

    lines_out.append('function drop(ev) {')
    lines_out.append('    ev.preventDefault();')
    lines_out.append('    var data = ev.dataTransfer.getData("text");')
    lines_out.append('    ev.target.appendChild(document.getElementById(data));')

    lines_out.append('  if (ev.target.id != "div_in")')
    lines_out.append('  {')
    lines_out.append('    var divNode = document.getElementById(ev.target.id);')
    lines_out.append('    var inputNodes = divNode.getElementsByTagName('+'\'input\''+');')
    lines_out.append('    inputNodes[0].value = data')
    lines_out.append('  }')
    lines_out.append('}')

    lines_out.append('function myFunction() {')
    lines_out.append('  var id;')
    lines_out.append('  var result = "";')
    lines_out.append('  for (id = 1; id <= 148; id++) {')
    lines_out.append('    divName = "div" + id')
    lines_out.append('    var divNode = document.getElementById(divName);')
    lines_out.append('    var inputNodes = divNode.getElementsByTagName('+'\'input\''+');')
    lines_out.append('    result = result + divName + " " + inputNodes[0].value' + '+'+ '"\\' + 'n"')
    lines_out.append('  }')
    lines_out.append('  var file = new File([result], "video_prop_yourname.txt", {type: "text/plain;charset=utf-8"});')
    lines_out.append('  saveAs(file);')
    lines_out.append('}')
    lines_out.append('</script>')

    lines_out.append('</body>')
    lines_out.append('<html>')

    fout.write('%s' % ('\n'.join(lines_out)))
    fout.close()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dirs', nargs='+', type=str)
  parser.add_argument('--out_dir', type=str)
  parser.add_argument('--scale', type=float, default=1.0)

  args = parser.parse_args()
  if args.data_dirs is not None and len(args.data_dirs) > 0 and args.out_dir is not None:
    gen_html(args.data_dirs, args.out_dir, args.scale)
  else:
    print('Example: python gen_html_video.py --out_dir . --data_dirs input gt single_0930')