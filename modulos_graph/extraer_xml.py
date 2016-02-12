# -*- coding: utf-8 -*-

import simple_xpath as x
import os
import re

#DIRECTORIO DOS LOGS

def extraer_xml(dir_log):

	arg_a_extraer = raw_input("arg: ")
	
	if arg_a_extraer.isdigit():
		arg_a_extraer = "arg"+arg_a_extraer

	doc_list = os.listdir(dir_log)
	doc_list = filter(lambda x: re.findall("log.+\.xml",x),doc_list)

	benchmark_info = []

	for doc in doc_list:
		xml = x.xml2element_list(dir_log+"/"+doc)
		datos = x.xpath_xmllist("root/execucion",xml,True)
		for dato in datos:
			if dato.name == "execucion":
				size = dato.attributes[arg_a_extraer][0]
			else:
				benchmark_info.append(
								[dato.attributes["nome"][0].split('"')[1],
								size.split('"')[1],
								dato.value.split("s")[0]]
								)

	benchmark_info = sorted(benchmark_info,key=lambda x: x[0])
	
	return benchmark_info

#extraer_xml(".")