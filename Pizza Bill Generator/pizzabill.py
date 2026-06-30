import random
price=0
pizza=int(input("enter choice of pizza[1.Normal,2.Deluxe]"))
if pizza== 1:
    v=int(input("veg or nonveg[1.Veg,2.Non veg]"))
    if v==1:
        price=300
        print("veg pizza given")
        c=int(input('do you want extra cheese?[1.Yes,2.No]'))
        if c==1:
            price+=100
            print('extra cheese added')
        if c==2:
            print('extra cheese not added')
        t=int(input('do you want extra toppings[1.Yes,2.No]'))
        if t==1:
            price+=100
            print('extra toppings given')
        if t==2:
            print('extra toppings not given')
        w=int(input('do you want any water bottles [1.yes,2.No]'))
        if w==1:
            wb=int(input('how many bottles'))
            wb_price=wb*20
            print(f'{wb} no. of water bottles served')
            price+=wb_price
        if w==2:
            print('no water bottles given')
        k=int(input('do you want any ketchup packets[1.Yes,2.No]'))
        if k==1:
            kb_packet=int(input('how many packets'))
            kb_price=kb_packet*5
            print(f'{kb_packet} no. of packets served')
            price+=kb_price
        if k==2:
            print('no ketchup packets given')
        sft=int(input('do you want any soft drinks[1.Yes,2.No]'))
        if sft==1:
            sft_pack=int(input('how many cans you want'))
            sft_price=sft_pack*75
            print(f'{sft_pack} no. of cans served')
            price+=sft_price
        if sft==2:
            print('no soft drinks served')
        take=int(input('is there any takeaway[1.Yes,2.No]'))
        if take==1:
            print('carry bag given')
            price+=20
        if take==2:
            print('carry bags not generated')
    if v==2:
        price=400
        print("non veg pizza given")
        c=int(input('do you want extra cheese?[1.Yes,2.No]'))
        if c==1:
            price+=100
            print('extra cheese added')
        if c==2:
            print('extra cheese not added')
        t=int(input('do you want extra toppings[1.Yes,2.No]'))
        if t==1:
            price+=100
            print('extra toppings given')
        if t==2:
            print('extra toppings not given')
        w=int(input('do you want any water bottles [1.yes,2.No]'))
        if w==1:
            wb=int(input('how many bottles'))
            wb_price=wb*20
            print(f'{wb} no. of water bottles served')
            price+=wb_price
        if w==2:
            print('no water bottles given')
        k=int(input('do you want any ketchup packets[1.Yes,2.No]'))
        if k==1:
            kb_packet=int(input('how many packets'))
            kb_price=kb_packet*5
            print(f'{kb_packet} no. of packets served')
            price+=kb_price
        if k==2:
            print('no ketchup packets given')
        sft=int(input('do you want any soft drinks[1.Yes,2.No]'))
        if sft==1:
            sft_pack=int(input('how many cans you want'))
            sft_price=sft_pack*75
            print(f'{sft_pack} no. of cans served')
            price+=sft_price
        if sft==2:
            print('no soft drinks served')
        take=int(input('is there any takeaway[1.Yes,2.No]'))
        if take==1:
            print('carry bag given')
            price+=20
        if take==2:
            print('carry bags not generated')
if pizza==2:
    v=int(input("veg or nonveg[1.Veg,2.Non Veg]"))
    if v==1:
        price=600
        print("veg pizza given")
        c=int(input('do you want extra cheese?[1.Yes,2.No]'))
        if c==1:
            price+=100
            print('extra cheese added')
        if c==2:
            print('extra cheese not added')
        t=int(input('do you want extra toppings[1.Yes,2.No]'))
        if t==1:
            price+=100
            print('extra toppings given')
        if t==2:
            print('extra toppings not given')
        w=int(input('do you want any water bottles [1.yes,2.No]'))
        if w==1:
            wb=int(input('how many bottles'))
            wb_price=wb*20
            print(f'{wb} no. of water bottles served')
            price+=wb_price
        if w==2:
            print('no water bottles given')
        k=int(input('do you want any ketchup packets[1.Yes,2.No]'))
        if k==1:
            kb_packet=int(input('how many packets'))
            kb_price=kb_packet*5
            print(f'{kb_packet} no. of packets served')
            price+=kb_price
        if k==2:
            print('no ketchup packets given')
        sft=int(input('do you want any soft drinks[1.Yes,2.No]'))
        if sft==1:
            sft_pack=int(input('how many cans you want'))
            sft_price=sft_pack*75
            print(f'{sft_pack} no. of cans served')
            price+=sft_price
        if sft==2:
            print('no soft drinks served')
        take=int(input('is there any takeaway[1.Yes,2.No]'))
        if take==1:
            print('carry bag given')
            price+=20
        if take==2:
            print('carry bags not generated')
    if v==2:
        price=800
        print("non veg pizza given")
        c=int(input('do you want extra cheese?[1.Yes,2.No]'))
        if c==1:
            price+=100
            print('extra cheese added')
        if c==2:
            print('extra cheese not added')
        t=int(input('do you want extra toppings[1.Yes,2.No]'))
        if t==1:
            price+=100
            print('extra toppings given')
        if t==2:
            print('extra toppings not given')
        w=int(input('do you want any water bottles [1.yes,2.No]'))
        if w==1:
            wb=int(input('how many bottles'))
            wb_price=wb*20
            print(f'{wb} no. of water bottles served')
            price+=wb_price
        if w==2:
            print('no water bottles given')
        k=int(input('do you want any ketchup packets[1.Yes,2.No]'))
        if k==1:
            kb_packet=int(input('how many packets'))
            kb_price=kb_packet*5
            print(f'{kb_packet} no. of packets served')
            price+=kb_price
        if k==2:
            print('no ketchup packets given')
        sft=int(input('do you want any soft drinks[1.Yes,2.No]'))
        if sft==1:
            sft_pack=int(input('how many cans you want'))
            sft_price=sft_pack*75
            print(f'{sft_pack} no. of cans served')
            price+=sft_price
        if sft==2:
            print('no soft drinks served')
        take=int(input('is there any takeaway[1.Yes,2.No]'))
        if take==1:
            print('carry bag given')
            price+=20
        if take==2:
            print('carry bags not generated')


print('*****************************************************')
print('Bill no.',random.randint(1000, 9999))
print(f'final price before gst is {price}')
gst=price*0.18
net_price=gst+price
print(f'net price before discount is {net_price}')
if net_price>3000:
    net_price=net_price-(net_price*0.12)
elif net_price>2000:
    net_price=net_price-(net_price*0.1)
elif net_price>1000:
    net_price=net_price-(net_price*0.05)
else:
    net_price=net_price-(net_price*0.2)
    
print(f'net amount to be paid is {net_price}')
print('*******************************************************')
