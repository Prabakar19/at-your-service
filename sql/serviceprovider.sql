--SERVICEPROVIDER TABLE
create table atyourservice.serviceprovider (
	service_provider_id uuid not null default uuid_generate_v1() primary key,
	company_name varchar(200),
    owner_name varchar(100),
    email_id varchar(100),
    contact_number varchar(50),
    password varchar(500),
    sp_rating float)
