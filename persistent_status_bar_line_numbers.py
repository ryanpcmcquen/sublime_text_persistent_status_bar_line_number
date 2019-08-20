import sublime
import sublime_plugin


class PersistentStatusBarLineNumbers(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        # def run(self, edit):
        # In the console this is given as:
        # view.rowcol(view.sel()[0].begin())[0] + 1
        current_line_number = view.rowcol(
            view.sel()[0].begin()
        )[0] + 1
        view.set_status('persistent_line_number', str(current_line_number))
