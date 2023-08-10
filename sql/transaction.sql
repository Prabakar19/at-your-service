--TRANSACTION TABLE
create table atyourservice.transaction (
	transaction_id uuid not null default uuid_generate_v1() primary key,
	billing_id uuid,
	service_id uuid,
    transaction_time timestamp,
    transaction_amount float,
    transaction_rating float,
    original_cost float)

alter table atyourservice.transaction add constraint fk_transaction_service
foreign key (service_id) references atyourservice.service(service_id)

alter table atyourservice.transaction add constraint fk_transaction_billing
foreign key (billing_id) references atyourservice.billing(billing_id)