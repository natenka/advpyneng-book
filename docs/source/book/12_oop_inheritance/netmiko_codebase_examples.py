#base_connection.py
    def commit(self):
        """Commit method for platforms that support this."""
        raise AttributeError("Network device does not support 'commit()' method")

    def save_config(self, *args, **kwargs):
        """Not Implemented"""
        raise NotImplementedError
