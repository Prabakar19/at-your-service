--SERVICE TABLE
create table atyourservice.service (
	service_id uuid not null default uuid_generate_v1() primary key,
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

alter table atyourservice.service add constraint fk_service_category
foreign key (category_id) references atyourservice.category(category_id)

alter table atyourservice.service add constraint fk_service_serviceprovider
foreign key (service_provider_id) references atyourservice.serviceprovider(service_provider_id)

alter table atyourservice.atyourservice.service add column service_name varchar(100);