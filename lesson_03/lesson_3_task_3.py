from address import Address
from mailing import Mailing

to_address = Address(101000, 'Москва', 'Мясницкая', 26, 14)
from_address = Address(620000, 'Екатеринбург', 'Ленина', 28, 45)

my_mailing = Mailing(to_address, from_address, 555, 'TRACK23456')

t = my_mailing.track
c = my_mailing.cost

f_ind = my_mailing.from_address.index
f_cit = my_mailing.from_address.city
f_str = my_mailing.from_address.street
f_hous = my_mailing.from_address.house
f_apt = my_mailing.from_address.apartment

t_ind = my_mailing.to_address.index
t_cit = my_mailing.to_address.city
t_str = my_mailing.to_address.street
t_hous = my_mailing.to_address.house
t_apt = my_mailing.to_address.apartment

print(
    'Отправление', t, 'из', f_ind, f_cit, f_str, f_hous, '-', f_apt,
    'в', t_ind, t_cit, t_str, t_hous, '-', t_apt,
    '. Стоимость', c, 'рублей'
    )
