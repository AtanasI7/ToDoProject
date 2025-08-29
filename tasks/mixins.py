class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO: Possible problem here
        for field in self.fields:
            self.fields[field].disabled = True