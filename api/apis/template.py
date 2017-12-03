from flask_restplus import Namespace, Resource
from catt.core.manager import TemplateFolderManager


# Defining the name space for Catt templates
api = Namespace('template',description='Allows to obtain information of the available templates.')

@api.route('/')
class TemplateList(Resource):

	def get(self):
		"""Returns a list of the available parallel pattern templates."""
		manager = TemplateFolderManager()
		data = {
			'template_list': manager.list_available_templates()
		}
		return data

@api.route('/detail/<string:name>')
class TemplateDetail(Resource):

	def get(self,name):
		"""Retunrs template info given its name."""
		manager = TemplateFolderManager()
		data = {
			'template_datail': manager.get_template_info()
		}
		return data