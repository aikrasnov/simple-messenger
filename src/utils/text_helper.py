class TextHelper:
    @staticmethod
    def hide_sensitive_data(string: str, count: int = 4):
        """Replace sensitive data with asterisk, except last 4 symbols."""
        return f"{'*' * (len(string) - count)}{string[-count:]}"
