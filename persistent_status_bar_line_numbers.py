import sublime
import sublime_plugin


class PersistentStatusBarLineNumbers(sublime_plugin.TextCommand):
    def run(self, edit):
        # In the console this is given as:
        # view.rowcol(view.sel()[0].begin())[0] + 1
        current_line_number = self.view.rowcol(
            self.view.sel()[0].begin()
        )[0] + 1
        self.view.set_status('persistent_line_number', current_line_number)

