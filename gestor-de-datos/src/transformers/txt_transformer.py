#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: txt_transformer.py
# Capitulo: Flujo de Datos
# Autor(es): Oscar de Jesús Torres Rivera
# Version: 1.0.0 Abril 2024
# Descripción:
#
#   Este archivo define un procesador de datos que se encarga de transformar
#   y formatear el contenido de un archivo TXT
#-------------------------------------------------------------------------
from src.extractors.txt_extractor import TXTExtractor
import luigi, os, json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                lines = txt_file.readlines()
                for line in lines[1:]:
                    records = line.strip().split(';')
                    for record in records:
                        columns = record.split(',')
                        if len(columns) >= 8:  # Verifica si hay al menos 8 campos en la línea
                            entry = {
                                "description": columns[2],
                                "quantity": int(columns[3]),
                                "price": float(columns[5]),
                                "total": int(columns[3]) * float(columns[5]),
                                "invoice": columns[0],
                                "provider": columns[6],
                                "country": columns[7].strip()
                            }
                            result.append(entry)
        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath(os.path.abspath("loader.py")))
        result_dir = os.path.join(project_dir, "result")
        return luigi.LocalTarget(os.path.join(result_dir, "txt.json"))
