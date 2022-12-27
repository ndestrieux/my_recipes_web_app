class MongoDbRouter:
    nonrel_models = {"maillogs"}

    def db_for_read(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return "mongodb"
        return "default"

    def db_for_write(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return "mongodb"
        return "default"

    def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
        return model_name in self.nonrel_models
