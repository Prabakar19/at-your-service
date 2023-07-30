--TRANSACTION TABLE
create table atyourservice.transaction (
	transaction_id uuid not null default uuid_generate_v1(),
	billing_id uuid,
	service_id uuid,
	customer_id uuid,
    transaction_time timestamp,
    transaction_amount float,
    transaction_rating float,
    original_cost float)
