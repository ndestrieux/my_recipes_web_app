class EmailTemplate:
    SEPARATOR = 40 * "-"

    def __init__(self):
        self.base_subject = "{} shared a recipe with you!"
        self.base_content = (
            f"\n\n{self.SEPARATOR}\nPlease find the recipe in attachment"
        )

    def get_full_subject(self, username):
        return self.base_subject.format(username)

    def get_full_content(self, content):
        return content + self.base_content
