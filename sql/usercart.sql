--CUSTOMER TABLE
create table atyourservice.usercart (
	customer_id uuid not null,
	service_id uuid not null,
	created_time not null timestamp,
	primary key(customer_id, service_id))
