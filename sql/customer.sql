--CUSTOMER TABLE
create table atyourservice.customer (
	customer_id uuid not null default uuid_generate_v1() primary key,
	customer_name varchar(100) not null,
    first_name varchar(100) not null,
    last_name varchar(50),
    email_id varchar(100) not null,
    phone_number varchar(50) not null,
    password varchar(100))
