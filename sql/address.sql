--ADDRESS TABLE
create table atyourservice.address (
	address_id uuid not null default uuid_generate_v1() primary key,
	house_address varchar(500) not null,
    area varchar(500),
    city varchar(100),
    state varchar(100),
    country varchar(100),
    pincode varchar(50))

alter table atyourservice.address add column person_id uuid;

alter table atyourservice.address add constraint fk_customer_address
foreign key (person_id) references atyourservice.customer(customer_id)

alter table atyourservice.address add constraint fk_serviceprovider_address
foreign key (person_id) references atyourservice.serviceprovider(service_provider_id)
