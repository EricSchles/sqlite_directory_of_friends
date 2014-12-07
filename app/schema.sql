drop table if exists account_holder;
create table account_holder (
	id integer primary key autoincrement,
	email text not null,
	username text not null,
	phone text not null,
	password text null
);

drop table if exists contact;
create table contact (
	id integer primary key autoincrement,
	name text not null,
	phone text not null,
	username text not null,
	email text not null
);
