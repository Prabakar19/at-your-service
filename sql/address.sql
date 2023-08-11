--ADDRESS TABLE
create table atyourservice.address (
	address_id uuid not null default uuid_generate_v1() primary key,
	house_address varchar(500) not null,
    area varchar(500),
    city varchar(100),
    state varchar(100),
    country varchar(100),
    pincode varchar(50))

alter table atyourservice.address add column customer_id uuid;
alter table atyourservice.address add column service_provider_id uuid;

alter table atyourservice.address add constraint fk_address_customer
foreign key (customer_id) references atyourservice.customer(customer_id)

alter table atyourservice.address add constraint fk_address_serviceprovider
foreign key (service_provider_id) references atyourservice.serviceprovider(service_provider_id)
