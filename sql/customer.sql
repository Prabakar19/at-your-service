--CUSTOMER TABLE
create table atyourservice.customer (
	customer_id uuid not null,
	customer_name varchar(100) not null,
    first_name varchar(100) not null,
    last_name varchar(50),
    email_id varchar(100) not null,
    phone_number varchar(50) not null,
    password varchar(100))

alter table atyourservice.customer alter column customer_id set default uuid_generate_v1()

insert into atyourservice.customer(customer_name, first_name, last_name, email_id, phone_number, password)
values ('prabakar', 'praba', 'kar', 'peekapo@gmail.com', '9876543210', '12345678')
