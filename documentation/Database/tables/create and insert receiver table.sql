CREATE TABLE public.receiver
(
    id serial NOT NULL,
    name character varying(255) NOT NULL,
	email character varying(100),
	phone character varying(11),
	
    PRIMARY KEY (id)
);
insert into receiver("name",email,phone) values('Eduardo','eduardo@biopark.com','48912345687');
insert into receiver("name",email,phone) values('Maria','maria@biopark.com','41987654321');
insert into receiver("name",email,phone) values('João','joao@biopark.com','44999887766');
insert into receiver("name",email,phone) values('Jéssica','jessica@biopark.com','19999112233');


