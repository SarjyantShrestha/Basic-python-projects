import qrcode

class MyQR:
  def __init__(self, size:int, padding:int):
    self.qr = qrcode.QRCode(box_size=size, border=padding)

  def create_qr(self, fg, bg, file_name: str):
    user_input = input('Enter your text: ')

    try:
      self.qr.add_data(user_input)
      qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
      qr_image.save(file_name)

      print('Success {file_name}')

    except Exception as e:
      print(f'Error: {e}')

def main():
  myqr = MyQR(size=10, padding=10)
  myqr.create_qr(file_name='sample.png',
                 fg='black',
                 bg ='white')

if __name__ == '__main__':
  main()