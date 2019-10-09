from cutecharts.render.engine import RenderEngine


class Page(RenderEngine):
    def __init__(self):
        self._charts: list = []

    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def add(self, *charts):
        for c in charts:
            self._charts.append(c)

    def render(self, dest: str = "render.html", template_name: str = "page.html"):
        super().render(dest, template_name)
