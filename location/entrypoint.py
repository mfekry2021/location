from ._internal.cluster import Cluster


class EntryPoint:
	"""Gateway class to interact with private Cluster and Location classes."""

	def __init__(self):
		self.cluster = Cluster()

	def get_cluster_id(self, latitude, longitude, sub_cluster):
		"""
		get cluster or sub-cluster id based on provided latitude and longitude
		"""
		latitude_count = 16 if sub_cluster == 0 else 64
		longitude_count = 32 if sub_cluster == 0 else 128
		cluster = self.cluster.get_cluster(latitude, longitude, latitude_count, longitude_count)
		return cluster.get('id')
