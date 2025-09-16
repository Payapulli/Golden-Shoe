# Run this script to populate the database
import sqlite3

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(id, product_type_id, name, cost, details, image_file1, image_file2, image_file3, image_file4, size, stock):
    try:
        conn = sqlite3.connect('golden_shoe.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO product
                                  (pid, product_type_id, name, cost, details, image_file1, image_file2, image_file3, image_file4, size, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        if image_file1:
            img1 = convertToBinaryData(image_file1)
        else:
            img1=None
        if image_file2:
            img2 = convertToBinaryData(image_file2)
        else:
            img2=None
        if image_file3:
            img3 = convertToBinaryData(image_file3)
        else:
            img3=None
        if image_file4:
            img4 = convertToBinaryData(image_file4)
        else:
            img4=None
        # Convert data into tuple format
        data_tuple = (id, product_type_id, name, cost, details, img1, img2, img3, img4, size, stock)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

# Addidas Breaknet
# Size 7
insertBLOB(1, 1, "Addidas Breaknet", "49.99", 
"Stay clear of foot faults on and off the court in these tennis-inspired shoes. The adidas shoes have a classic 3-Stripes upper for a timeless look. They're built for comfort with a soft sockliner and textile lining.", 
"app/static/images/addidas_breaknet/addidas_breaknet.jpeg", "app/static/images/addidas_breaknet/addidas_breaknet2.jpg", 
"app/static/images/addidas_breaknet/addidas_breaknet3.jpg", "app/static/images/addidas_breaknet/addidas_breaknet4.jpg", 7, 20)
# Size 8
insertBLOB(2, 1, "Addidas Breaknet", "49.99", 
"Stay clear of foot faults on and off the court in these tennis-inspired shoes. The adidas shoes have a classic 3-Stripes upper for a timeless look. They're built for comfort with a soft sockliner and textile lining.", 
"app/static/images/addidas_breaknet/addidas_breaknet.jpeg", "app/static/images/addidas_breaknet/addidas_breaknet2.jpg", 
"app/static/images/addidas_breaknet/addidas_breaknet3.jpg", "app/static/images/addidas_breaknet/addidas_breaknet4.jpg", 8, 20)
# Size 9
insertBLOB(3, 1, "Addidas Breaknet", "49.99", 
"Stay clear of foot faults on and off the court in these tennis-inspired shoes. The adidas shoes have a classic 3-Stripes upper for a timeless look. They're built for comfort with a soft sockliner and textile lining.", 
"app/static/images/addidas_breaknet/addidas_breaknet.jpeg", "app/static/images/addidas_breaknet/addidas_breaknet2.jpg", 
"app/static/images/addidas_breaknet/addidas_breaknet3.jpg", "app/static/images/addidas_breaknet/addidas_breaknet4.jpg", 9, 20)

# Air Max 95
# Size 7
insertBLOB(4, 2, "Air Max 95", "49.99", 
"Taking inspiration from the human body and '90s athletics aesthetics, the Air Max 95 mixes unbelievable comfort with fast-paced style. The wavy side panels add natural flow to any outfit, while visible Nike Air in the heel and forefoot delivers performance comfort.", 
"app/static/images/air_max95/air_max95.jpeg", "app/static/images/air_max95/air_max95_2.jpeg", 
"app/static/images/air_max95/air_max95_3.jpeg", "app/static/images/air_max95/air_max95_4.jpeg", 7, 20)
# Size 8
insertBLOB(5, 2, "Air Max 95", "49.99", 
"Taking inspiration from the human body and '90s athletics aesthetics, the Air Max 95 mixes unbelievable comfort with fast-paced style. The wavy side panels add natural flow to any outfit, while visible Nike Air in the heel and forefoot delivers performance comfort.", 
"app/static/images/air_max95/air_max95.jpeg", "app/static/images/air_max95/air_max95_2.jpeg", 
"app/static/images/air_max95/air_max95_3.jpeg", "app/static/images/air_max95/air_max95_4.jpeg", 8, 20)
# Size 9
insertBLOB(6, 2, "Air Max 95", "49.99", 
"Taking inspiration from the human body and '90s athletics aesthetics, the Air Max 95 mixes unbelievable comfort with fast-paced style. The wavy side panels add natural flow to any outfit, while visible Nike Air in the heel and forefoot delivers performance comfort.", 
"app/static/images/air_max95/air_max95.jpeg", "app/static/images/air_max95/air_max95_2.jpeg", 
"app/static/images/air_max95/air_max95_3.jpeg", "app/static/images/air_max95/air_max95_4.jpeg", 9, 20)

# Shein Black Heels
# Size 7
insertBLOB(7, 3, "Shein Black Heels", "49.99", 
"Minimalist Stiletto Heeled Ankle Strap Sandals", 
"app/static/images/black_heels/black_heels.jpg", "app/static/images/black_heels/black_heels2.jpg", 
"app/static/images/black_heels/black_heels3.jpg", "app/static/images/black_heels/black_heels4.jpg", 7, 20)
# Size 8
insertBLOB(8, 3, "Shein Black Heels", "49.99", 
"Minimalist Stiletto Heeled Ankle Strap Sandals", 
"app/static/images/black_heels/black_heels.jpg", "app/static/images/black_heels/black_heels2.jpg", 
"app/static/images/black_heels/black_heels3.jpg", "app/static/images/black_heels/black_heels4.jpg", 8, 20)
# Size 9
insertBLOB(9, 3, "Shein Black Heels", "49.99", 
"Minimalist Stiletto Heeled Ankle Strap Sandals", 
"app/static/images/black_heels/black_heels.jpg", "app/static/images/black_heels/black_heels2.jpg", 
"app/static/images/black_heels/black_heels3.jpg", "app/static/images/black_heels/black_heels4.jpg", 9, 20)

# Blue Suede Shoes
# Size 7
insertBLOB(10, 4, "Blue Suede Shoes", "49.99", 
"Crafted from high-end, raw materials, it features lightweight cushion technology, the perfectly-weighted rubber sole, and classic cap-toe design for a crazy-comfy, go-to look.", 
"app/static/images/blue_suede/blue_suede.jpg", "app/static/images/blue_suede/blue_suede2.jpg", 
"app/static/images/blue_suede/blue_suede3.jpg", "app/static/images/blue_suede/blue_suede4.jpg", 7, 20)
# Size 8
insertBLOB(11, 4, "Blue Suede Shoes", "49.99", 
"Crafted from high-end, raw materials, it features lightweight cushion technology, the perfectly-weighted rubber sole, and classic cap-toe design for a crazy-comfy, go-to look.", 
"app/static/images/blue_suede/blue_suede.jpg", "app/static/images/blue_suede/blue_suede2.jpg", 
"app/static/images/blue_suede/blue_suede3.jpg", "app/static/images/blue_suede/blue_suede4.jpg", 8, 20)
# Size 9
insertBLOB(12, 4, "Blue Suede Shoes", "49.99", 
"Crafted from high-end, raw materials, it features lightweight cushion technology, the perfectly-weighted rubber sole, and classic cap-toe design for a crazy-comfy, go-to look.", 
"app/static/images/blue_suede/blue_suede.jpg", "app/static/images/blue_suede/blue_suede2.jpg", 
"app/static/images/blue_suede/blue_suede3.jpg", "app/static/images/blue_suede/blue_suede4.jpg", 9, 20)

# Brogue Ankle Boots
# Size 7
insertBLOB(13, 5, "Brogue Ankle Boots", "49.99", 
"Yasmine Tan. Beautifully crafted in Italian tan leather with broguing throughout.", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots2.jpg", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots3.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots4.jpg", 7, 20)
# Size 8
insertBLOB(14, 5, "Brogue Ankle Boots", "49.99", 
"Yasmine Tan. Beautifully crafted in Italian tan leather with broguing throughout.", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots2.jpg", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots3.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots4.jpg", 8, 20)
# Size 9
insertBLOB(15, 5, "Brogue Ankle Boots", "49.99", 
"Yasmine Tan. Beautifully crafted in Italian tan leather with broguing throughout.", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots2.jpg", 
"app/static/images/brogue_ankle_boots/brogue_ankle_boots3.jpg", "app/static/images/brogue_ankle_boots/brogue_ankle_boots4.jpg", 9, 20)

# Cassia white trainers
# Size 7
insertBLOB(16, 6, "Cassia white trainers", "49.99", 
"Break the mould with this first-of-its-kind design. Our Cassia dresses up a progressive, feminine silhouette with a mesh base and slightly oversized leather panels.", 
"app/static/images/cassia_trainers/cassia_trainers.jpg", "app/static/images/cassia_trainers/cassia_trainers2.jpg", 
"app/static/images/cassia_trainers/cassia_trainers3.jpg", "app/static/images/cassia_trainers/cassia_trainers4.jpg", 7, 20)
# Size 8
insertBLOB(17, 6, "Cassia white trainers", "49.99", 
"Break the mould with this first-of-its-kind design. Our Cassia dresses up a progressive, feminine silhouette with a mesh base and slightly oversized leather panels.", 
"app/static/images/cassia_trainers/cassia_trainers.jpg", "app/static/images/cassia_trainers/cassia_trainers2.jpg", 
"app/static/images/cassia_trainers/cassia_trainers3.jpg", "app/static/images/cassia_trainers/cassia_trainers4.jpg", 8, 20)
# Size 9
insertBLOB(18, 6, "Cassia white trainers", "49.99", 
"Break the mould with this first-of-its-kind design. Our Cassia dresses up a progressive, feminine silhouette with a mesh base and slightly oversized leather panels.", 
"app/static/images/cassia_trainers/cassia_trainers.jpg", "app/static/images/cassia_trainers/cassia_trainers2.jpg", 
"app/static/images/cassia_trainers/cassia_trainers3.jpg", "app/static/images/cassia_trainers/cassia_trainers4.jpg", 9, 20)

# New Balance Trainers
# Size 7
insertBLOB(19, 7, "New Balance Trainers", "49.99", 
"The men's 574 is iconic. With clean and classic lines, this die cut EVA sneaker makes a standout, everyday statement.", 
"app/static/images/new_balance/new_balance.jpg", "app/static/images/new_balance/new_balance2.jpg", 
"app/static/images/new_balance/new_balance3.jpg", "app/static/images/new_balance/new_balance4.jpg", 7, 20)
# Size 8
insertBLOB(20, 7, "New Balance Trainers", "49.99", 
"The men's 574 is iconic. With clean and classic lines, this die cut EVA sneaker makes a standout, everyday statement.", 
"app/static/images/new_balance/new_balance.jpg", "app/static/images/new_balance/new_balance2.jpg", 
"app/static/images/new_balance/new_balance3.jpg", "app/static/images/new_balance/new_balance4.jpg", 8, 20)
# Size 7
insertBLOB(21, 7, "New Balance Trainers", "49.99", 
"The men's 574 is iconic. With clean and classic lines, this die cut EVA sneaker makes a standout, everyday statement.", 
"app/static/images/new_balance/new_balance.jpg", "app/static/images/new_balance/new_balance2.jpg", 
"app/static/images/new_balance/new_balance3.jpg", "app/static/images/new_balance/new_balance4.jpg", 9, 20)

# Ted Baker leather shoes
# Size 7
insertBLOB(22, 8, "Ted Baker leather shoes", "49.99", 
"A classic brogue, these are an essential item of footwear that belongs in everyone’s collection.", 
"app/static/images/ted_baker_leather/ted_baker_leather.jpg", "app/static/images/ted_baker_leather/ted_baker_leather2.jpg", 
"app/static/images/ted_baker_leather/ted_baker_leather3.jpg", "app/static/images/ted_baker_leather/ted_baker_leather4.jpg", 7, 20)
# Size 8
insertBLOB(23, 8, "Ted Baker leather shoes", "49.99", 
"A classic brogue, these are an essential item of footwear that belongs in everyone’s collection.", 
"app/static/images/ted_baker_leather/ted_baker_leather.jpg", "app/static/images/ted_baker_leather/ted_baker_leather2.jpg", 
"app/static/images/ted_baker_leather/ted_baker_leather3.jpg", "app/static/images/ted_baker_leather/ted_baker_leather4.jpg", 8, 20)
# Size 9
insertBLOB(24, 8, "Ted Baker leather shoes", "49.99", 
"A classic brogue, these are an essential item of footwear that belongs in everyone’s collection.", 
"app/static/images/ted_baker_leather/ted_baker_leather.jpg", "app/static/images/ted_baker_leather/ted_baker_leather2.jpg", 
"app/static/images/ted_baker_leather/ted_baker_leather3.jpg", "app/static/images/ted_baker_leather/ted_baker_leather4.jpg", 9, 20)