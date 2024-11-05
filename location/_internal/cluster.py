class Cluster:

	def get_cluster(self, latitude, longitude, latitude_count, longitude_count):
		latitude = float(latitude)
		longitude = float(longitude)
		max_longitude = 180
		min_longitude = -180
		max_latitude = 85
		min_latitude = -85
		y_increment = (max_longitude - min_longitude) / longitude_count
		x_increment = (max_latitude - min_latitude) / latitude_count
		clusters = []
		current_id = 0
		x = min_longitude
		while min_longitude < max_longitude:
			j = min_latitude
			while j < max_latitude:
				clusters.append({
					'min_longitude': min_longitude,
					'max_longitude': min_longitude + y_increment,
					'min_latitude': j,
					'max_latitude': j + x_increment,
					'id': current_id
				})
				j += x_increment
				current_id += 1
			min_longitude += y_increment
		for cluster in clusters:
			if cluster['min_longitude'] <= longitude <= cluster['max_longitude'] and cluster[
				'min_latitude'] <= latitude <= \
					cluster['max_latitude']:
				return cluster
		return None
