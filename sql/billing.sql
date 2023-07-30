--BILLING TABLE
create table atyourservice.billing (
	billing_id uuid not null default uuid_generate_v1(),
	cost float,
    gst float,
    mrp_cost float,
    total_cost float,
    customer_id uuid not null,
    service_provider_id uuid not null)
