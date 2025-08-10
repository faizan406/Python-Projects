import qrone

#taling UPI ID as an input
upi_id=input("Enter your UPI ID= ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment URL ID based on the UPI ID and payment app
#You can modify these URLs based on the payment app you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR code for each payment app

phonepe_url=qrone.make(phonepe_url)
paytm_url=qrone.make(paytm_url)
google_pay_url=qrone.make(google_pay_url)

#save the QR code photo as file

phonepe_url.save('phonepe_url.png')
paytm_url.save('paytm_url.png')
google_pay_url.save('google_pay_url.png')

#display the QR code (you may need PIL/pillow libray)
phonepe_url.show()
paytm_url.show()
google_pay_url.show()