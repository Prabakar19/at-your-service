--CATEGORY TABLE
create table atyourservice.category (
	category_id uuid not null default uuid_generate_v1(),
	category_name varchar(100),
    category_pic varchar(100))