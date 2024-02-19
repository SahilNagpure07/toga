from org.osmdroid.views import MapView as OSMMapView

from .base import SimpleProbe


class MapViewProbe(SimpleProbe):
    native_class = OSMMapView
    # This is a little lower than ideal, but OSMDroid has something weird
    # going on where the fidelity of the map center appears to be related
    # to the map zoom level.
    location_threshold = 0.001

    async def latitude_span(self):
        return self.native.getLatitudeSpanDouble()

    @property
    def pin_count(self):
        # OSMDroid doesn't differentiate between markers and other overlays.
        # There's always 1 overlay for the copyright notice.
        return self.native.getOverlays().size() - 1

    async def select_pin(self, pin):
        self.impl.marker_click_listener.onMarkerClick(pin._native, self.native)
        await self.redraw(f"{pin.title} pin has been selected")
