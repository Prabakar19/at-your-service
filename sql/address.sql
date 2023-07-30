--ADDRESS TABLE
create table atyourservice.address (
	address_id uuid not null default uuid_generate_v1(),
	house_address varchar(500) not null,
    area varchar(500),
    city varchar(100),
    state varchar(100),
    country varchar(100),
    pincode varchar(50))


insert into atyourservice.address(house_address, area, city, state, country, pincode)
values ('102, silver spring', 'Kasavanahalli', 'Bangalore', 'Karnataka', 'India', '560035')
