CREATE TABLE public.send_schedule
(
    id serial NOT NULL,
    status_id integer NOT NULL,
    type_id integer NOT NULL,
    receiver_id integer NOT NULL,
    date_time timestamp without time zone NOT NULL,
    message text,
    PRIMARY KEY (id),
    FOREIGN KEY (status_id) REFERENCES public.send_status (id),
	FOREIGN KEY (type_id) REFERENCES public.send_type (id),
	FOREIGN KEY (receiver_id) REFERENCES public.receiver (id)
);

insert into send_schedule(status_id,type_id,receiver_id,date_time, "message")
values(1,4,1,'2020-12-21 11:42:55'::timestamp,'teste');

