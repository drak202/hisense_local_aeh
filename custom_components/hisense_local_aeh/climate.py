async def async_setup_entry(hass, entry, async_add_entities):
    host = entry.data["host"]
    name = entry.data.get("name", "Hisense Klima")
    # Pokračuj v inicializácii zariadenia s použitím host a name
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVAC_MODE_OFF, HVAC_MODE_COOL
from homeassistant.const import TEMP_CELSIUS

class HisenseClimate(ClimateEntity):
    def __init__(self, name, host):
        self._name = name
        self._host = host
        self._temperature = 24
        self._hvac_mode = HVAC_MODE_COOL

    @property
    def name(self):
        return self._name

    @property
    def temperature_unit(self):
        return TEMP_CELSIUS

    @property
    def hvac_mode(self):
        return self._hvac_mode

    @property
    def hvac_modes(self):
        return [HVAC_MODE_OFF, HVAC_MODE_COOL]

    async def async_set_hvac_mode(self, hvac_mode):
        self._hvac_mode = hvac_mode
        # TODO: send command to device
        self.async_write_ha_state()

async def async_setup_entry(hass, entry, async_add_entities):
    host = entry.data["host"]
    name = entry.data.get("name", "Hisense Klima")
    async_add_entities([HisenseClimate(name, host)])
