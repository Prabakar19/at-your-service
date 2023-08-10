--BILLING TABLE
create table atyourservice.billing (
	billing_id uuid not null default uuid_generate_v1() primary key,
	cost float,
    gst float,
    mrp_cost float,
    total_cost float,
    customer_id uuid not null,
    service_provider_id uuid not null)

alter table atyourservice.billing add constraint fk_billing_customer
foreign key (customer_id) references atyourservice.customer(customer_id)

alter table atyourservice.billing add constraint fk_billing_serviceprovider
foreign key (service_provider_id) references atyourservice.serviceprovider(service_provider_id)