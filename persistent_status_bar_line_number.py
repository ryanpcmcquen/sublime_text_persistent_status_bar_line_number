import sublime
import sublime_plugin


class PersistentStatusBarLineNumber(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        current_line_number = view.rowcol(
            view.sel()[0].begin()
        )[0] + 1
        view.set_status('persistent_line_number', str(current_line_number))
