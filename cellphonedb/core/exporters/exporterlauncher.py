import inspect

from cellphonedb.core.exporters import ligands_receptors_proteins_exporter, complex_exporter, complex_web_exporter


class ExporterLauncher(object):
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def ligands_receptors_proteins(self):
        genes_expanded = self.database_manager.get_repository('gene').get_all_expanded()
        return ligands_receptors_proteins_exporter.call(genes_expanded)

    def complex(self):
        complexes = self.database_manager.get_repository('complex').get_all()
        multidatas = self.database_manager.get_repository('multidata').get_all()
        complex_compositions = self.database_manager.get_repository('complex').get_all_compositions()
        proteins = self.database_manager.get_repository('protein').get_all()

        return complex_exporter.call(complexes, multidatas, complex_compositions, proteins)


def complex_web(self, output_name=None):
    complexes = self.database_manager.get_repository('complex').get_all()
    multidatas = self.database_manager.get_repository('multidata').get_all()
    complex_compositions = self.database_manager.get_repository('complex').get_all_compositions()
    proteins = self.database_manager.get_repository('protein').get_all()

    return complex_web_exporter.call(complexes, multidatas, complex_compositions, proteins)

# def interaction(self, output_name=None):
#     if not output_name:
#         current_method_name = inspect.getframeinfo(inspect.currentframe()).function
#         output_name = '%s.csv' % current_method_name
#
#     result = interaction_exporter.call()
#     result.to_csv('out/%s' % output_name, index=False)
#
# def receptor_ligand_interaction(self, output_name=None):
#     if not output_name:
#         current_method_name = inspect.getframeinfo(inspect.currentframe()).function
#         output_name = '%s.csv' % current_method_name
#
#     result = receptor_ligand_interaction_exporter.call()
#     result.to_csv('out/%s' % output_name, index=False)
#
# def protein(self, output_name=None):
#     if not output_name:
#         current_method_name = inspect.getframeinfo(inspect.currentframe()).function
#         output_name = '%s.csv' % current_method_name
#
#     proteins_query = db.session.query(Protein)
#     multidata_query = db.session.query(Multidata)
#
#     proteins_df = pd.read_sql(proteins_query.statement, db.engine)
#     multidata_df = pd.read_sql(multidata_query.statement, db.engine)
#
#     proteins_multidata = pd.merge(proteins_df, multidata_df, left_on='protein_multidata_id',
#                                   right_on='id_multidata')
#
#     proteins_multidata.drop(['id_multidata', 'id_protein', 'protein_multidata_id'], axis=1, inplace=True)
#
#     proteins_multidata.rename(index=str, columns={'name': 'uniprot'}, inplace=True)
#
#     proteins_multidata = dataframe_format.bring_columns_to_start(['uniprot'], proteins_multidata)
#     proteins_multidata = dataframe_format.bring_columns_to_end(['tags', 'tags_reason'], proteins_multidata)
#     proteins_multidata.to_csv('out/%s' % output_name, index=False)
#
# def gene(self, output_name=None):
#     if not output_name:
#         current_method_name = inspect.getframeinfo(inspect.currentframe()).function
#         output_name = '%s.csv' % current_method_name
#
#     gene_query = db.session.query(Gene, Multidata.name).join(Protein).join(Multidata)
#     gene_df = pd.read_sql(gene_query.statement, db.engine)
#
#     filters.remove_not_defined_columns(gene_df, database.get_column_table_names(Gene, db) + ['name'])
#
#     gene_df.drop(['id_gene', 'protein_id'], axis=1, inplace=True)
#
#     gene_df.rename(index=str, columns={'name': 'uniprot'}, inplace=True)
#
#     gene_df.to_csv('out/%s' % output_name, index=False)
