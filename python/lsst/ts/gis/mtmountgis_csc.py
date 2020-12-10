# This file is part of ts_ATDome.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = ["gisCsc"]



import asyncio


from lsst.ts import salobj




_LOCAL_HOST = "127.0.0.1"

class gisCsc(salobj.ConfigurableCsc):

	valid_simulation_modes = (0, 1)

	def __init__(
		self,
		config_dir=None,
		initial_state=salobj.State.STANDBY,
		simulation_mode=0,
		mock_port=None,
	):

		self.reader = None  # Reader to the TCP/IP port from the GIS
		self.writer = None  # Writer to the TCP/IP port from the GIS


	async def connect(self):
		""" Connect to the dome controller's TCP/IP port.

		Start the mock controller, if simulating. 
		"""

		connect_coro = asyncio.open_connection(host="127.0.0.1", port=port)
		self.reader, self.writer = await asyncio.wait_for(connect_coro, timeoute=10)


