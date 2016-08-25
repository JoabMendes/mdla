--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.13
-- Dumped by pg_dump version 9.3.13
-- Started on 2016-08-25 11:23:21 BRT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 822 (class 1259 OID 206037)
-- Name: a_selected_courses; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE a_selected_courses (
    course bigint,
    activity bigint,
    fullname character varying(254)
);


ALTER TABLE public.a_selected_courses OWNER TO postgres;

--
-- TOC entry 3788 (class 0 OID 206037)
-- Dependencies: 822
-- Data for Name: a_selected_courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY a_selected_courses (course, activity, fullname) FROM stdin;
344	165247	Fundamentos da Gestão Pública - TGP0002_1_2013.2
266	154231	DISCIPLINA EDUCAÇÃO A DISTÂNCIA E INFORMÁTICA BÁSICA - TGP0001_2013.1
233	89911	Atividades Acadêmico-Científico-Culturais (AACC)
376	89495	Introdução à Economia - TGP0003_1_2013.2
250	89305	DISCIPLINA EDUCAçãO INCLUSIVA - FPD1002_2013.1 SUZANA copiar 1
204	84696	Educação Inclusiva PEDAGOGIA
305	81693	Contabilidade Pública - TGP0008_1_2013.2
427	81383	Seminário Temático II - TGP0012_1_2013.2
7	79823	Licenciatura em Pedagogia
378	77494	Introdução ao Direito Constitucional - TGP0004_1_2013.2
392	76364	Metodologia das Artes Marciais - DEF1016_1_2013.2
265	75139	Gestão Pública
195	74942	Educação e Tecnologia
267	72395	DISCIPLINA SEMINÁRIO TEMÁTICO I - TGP0006_2013.1
10	72102	Bacharelado em Administração Pública
2	69066	Licenciatura em Ciências Biologicas
202	68824	Metodologia Científica
412	68358	Psicologia da Educação II - FPD1005_1_2013.2
100	62056	DISCIPLINA ORGANIZAçãO DO ESPAçO - DGD0002_2013.1
451	61301	Didática e Ensino de Geografia - DGD0009_1_2013.2
194	60925	Psicologia da Educação - LETRAS
154	60227	DISCIPLINA FONéTICA E FONOLOGIA DA LíNGUA PORTUGUESA - LET2006_2013.1
99	56953	DISCIPLINA LEITURAS CARTOGRÁFICAS E INTERPRETAÇÕES ESTATÍSTICAS I - DGD0003_2013.1
94	54783	Educação e Tecnologia
333	54287	Estudos Contemporâneos da Cultura - DGD0007_1_2013.2
413	54255	Psicologia da Educação II - FPD1005_2_2013.2
319	53803	Elaboração e Administração de Projetos - ADM1025_1_2013.2
280	53683	Alfabetização e Letramento - FPD1006_2_2013.2
88	52988	Tecnologia e Informação
203	51208	Psicologia da Educação - Suenyra
142	50950	DISCIPLINA EDUCAçãO INCLUSIVA - FPD1002_2013.1
197	50440	Educação e Tecnologia
147	50423	Gestão de Pessoas no Setor Público II
431	49676	Teorias e Práticas Curriculares - PED1008_2_2013.2
132	48945	Fundamentos da Educação 
137	48906	DISCIPLINA POLíTICA E ORGANIZAçãO DA EDUCAçãO BáSICA NO BRASIL - FPD1004_2013.1
249	48726	DISCIPLINA EDUCAÇÃO INCLUSIVA - FPD1002_2013.1
201	47608	Fundamentos da Educação
379	46838	Introdução aos Estudos da Linguagem - FPD1007_1_2013.2
89	46595	Estágio Supervisionado III
9	45529	 Licenciatura em Matemática
121	45057	DISCIPLINA GEOGRAFIA FíSICA I - DGD0005_2013.1
\.


-- Completed on 2016-08-25 11:23:22 BRT

--
-- PostgreSQL database dump complete
--

