async def async_setup_entry(hass, entry, async_add_entities):
    host = entry.data["host"]
    name = entry.data.get("name", "Hisense Klima")
    # Pokračuj v inicializácii zariadenia s použitím host a name
