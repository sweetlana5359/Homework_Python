from smartphone import Smartphone

catalog = [
   Smartphone('Apple', 'iPhone 18 Pro', '+79987654321'),
   Smartphone('Xiaomi', '13 Pro', '+79912345678'),
   Smartphone('Samsung', 'Galaxy S26 Ultra', '+79623456789'),
   Smartphone('Huawei', 'Mate 80 Pro', '+79345678122'),
   Smartphone('Nokia', 'XR21', '+79864275310')
]


for phone in catalog:
    print(phone.brand, '-', phone.model, '.', phone.phone_number)
