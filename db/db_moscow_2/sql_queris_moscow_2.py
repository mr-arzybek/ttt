# =======================================================================================================================

CREATE_PRODUCT_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY,
    name_ VARCHAR(255),
    date_coming VARCHAR(15),
    date_care VARCHAR(15),
    name_customer VARCHAR(255),
    phone VARCHAR(50),
    name_salesman VARCHAR(255),
    price DECIMAL(10, 2),
    discount INTEGER,
    total_price INTEGER,
    city VARCHAR(50)
    )
"""

PRODUCT_INSERT_QUERY = """
    INSERT OR IGNORE INTO products 
    (name_, date_coming, date_care, name_customer, phone, name_salesman, price, discount, total_price, city)
    VALUES (?,?,?,?,?,?,?,?,?,?)
"""

# =======================================================================================================================

CREATE_BOOKING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS booking
    (name_product VARCHAR(255),
    start_of_armor VARCHAR(255),
    end_of_armor VARCHAR(255),
    name_customer VARCHAR(255),
    phone VARCHAR(50),
    name_salesman VARCHAR(255),
    price DECIMAL(10, 2),
    discount INTEGER,
    total_price INTEGER,
    city VARCHAR(50)
    )
"""

BOOKING_INSERT_QUERY = """
    INSERT OR IGNORE INTO booking  
    (name_product, start_of_armor, end_of_armor, name_customer, phone, name_salesman, price, discount, total_price, city)
    VALUES (?,?,?,?,?,?,?,?,?, ?)
"""

# =======================================================================================================================

CREATE_STAFF_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS staff
    (full_name_staff VARCHAR(255),
    phone_staff VARCHAR(50) UNIQUE,
    schedule_staff VARCHAR(255),
    city_staff VARCHAR(50)
    )
"""

STAFF_INSERT_QUERY = """
    INSERT OR IGNORE INTO staff  
    (full_name_staff, phone_staff, schedule_staff, city_staff)
    VALUES (?,?,?,?)
"""

# =======================================================================================================================

CREATE_BEING_LATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS being_late
    (full_name VARCHAR(255),
    date_ VARCHAR(50),
    time_ VARCHAR(255),
    city VARCHAR(50)
    )
"""

BEING_LATE_INSERT_QUERY = """
    INSERT OR IGNORE INTO being_late  
    (full_name, date_, time_, city)
    VALUES (?,?,?,?)
"""
