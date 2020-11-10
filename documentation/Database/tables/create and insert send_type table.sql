CREATE TABLE public.send_type
(
    id serial NOT NULL,
    type character varying(100) NOT NULL,
    PRIMARY KEY (id)
);
insert into send_type("type") values('email');
insert into send_type("type") values('sms');
insert into send_type("type") values('push');
insert into send_type("type") values('whatsapp');


