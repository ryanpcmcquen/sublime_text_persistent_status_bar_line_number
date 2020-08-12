import sublime
import sublime_plugin


class PersistentStatusBarLineNumber(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        try:
            current_line_number = view.rowcol(
                view.sel()[0].begin()
            )[0] + 1
            view.set_status('persistent_line_number', str(current_line_number))
        except IndexError:
            # Sometimes we just get weird indices. There's no
            # need to fill up the Sublime Console
            # with those errors.
            pass
