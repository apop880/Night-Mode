import appdaemon.plugins.hass.hassapi as hass

class NightMode(hass.Hass):

	def initialize(self):
		self.listen_state(self.night_toggle, "input_boolean.night_mode")
		#turn off night mode at sunrise
		self.run_at_sunrise(self.end_night_mode)
		self.prev_brightness = {}
		self.night_brightness = self.args['night_brightness']
		for light in self.split_device_list(self.args['light']):
			self.listen_state(self.brightness_on, light, new="on", old="off")
			self.prev_brightness[light] = 0
			
	def night_toggle(self, entity, attribute, old, new, kwargs):
		if new=="on" and old=="off":
			for light in self.split_device_list(self.args['light']):
				if self.get_state(light) == "on":
					if self.get_state(light, attribute="brightness") >= self.night_brightness:
						self.prev_brightness[light] = self.get_state(light, attribute="brightness")
					self.turn_on(light, brightness=self.night_brightness)
				else:
					self.prev_brightness[light] = 0
		elif new=="off" and old=="on":
			for light in self.split_device_list(self.args['light']):
				if self.get_state(light) == "on":
					if self.get_state(light, attribute="brightness") <= self.night_brightness and self.prev_brightness[light] > 0:
						self.turn_on(light, brightness=self.prev_brightness[light])
		
	def brightness_on(self, entity, attribute, old, new, kwargs):
		night_mode = self.get_state("input_boolean.night_mode")
		brightness = self.get_state(entity, attribute="brightness")
		if night_mode=="on" and brightness >= self.night_brightness:
			self.prev_brightness[entity] = self.get_state(entity, attribute="brightness")
			self.turn_on(entity, brightness=self.night_brightness)
		elif night_mode=="off" and brightness <= self.night_brightness:
			if self.prev_brightness[entity] > 0:
				self.turn_on(entity, brightness=self.prev_brightness[entity])

	def end_night_mode(self, kwargs):
		self.turn_off("input_boolean.night_mode")