drop table if exists account_holder;
create table account_holder (
	email text not null,
	username text primary key not null,
	phone text not null,
	password text null
);

drop table if exists contact;
create table contact (
	name text not null,
	phone text not null,
	username text foriegn key not null,
	email text not null
);
