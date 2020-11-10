CREATE TABLE public.send_status
(
    id serial NOT NULL,
    status character varying(100) NOT NULL,
    PRIMARY KEY (id)
);
insert into send_status("status") values('aguardando envio');
insert into send_status("status") values('enviando');
insert into send_status("status") values('erro ao envio');
insert into send_status("status") values('enviado');

