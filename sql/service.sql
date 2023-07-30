--SERVICE TABLE
create table atyourservice.service (
	service_id uuid not null default uuid_generate_v1(),
	cost float,
    discount float,
    discounted_cost float,
    discount_availability boolean,
    details varchar(1000),
    warranty float,
    service_provider_id uuid,
    category_id uuid,
    service_ratings float,
    rating float,
    service_pic varchar(50))
