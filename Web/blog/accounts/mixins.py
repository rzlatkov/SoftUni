class BootstrapifyFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bootstrapify()

    def bootstrapify(self):
        # field_name = verbose_name
        # field_obj is the actual instance of the field class
        for field_name, field_obj in self.fields.items():
            try:
                if 'class' not in field_obj.widget.attrs:
                    field_obj.widget.attrs['class'] = None
                field_obj.widget.attrs['class'] = 'form-control'
            except:
                continue
