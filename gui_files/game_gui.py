from appJar import gui as gui
import file_handler as fh
import input_functions as inpfunc

file_content = fh.file_reader(read_file="words.txt", encoding='ISO-8859-1')

def cp_gui():
    with gui("Ordspelet") as app:

        app.setSize(300, 400)
        app.setLocation(0, 0)

        app.startTabbedFrame("TabbedFrame")
        app.setTabbedFrameTabExpand("TabbedFrame", expand=True)
        app.startTab("Program vs. User")
        app.addLabel("ti_pro_usr", f"saker med grejer", column=0, row=0)
        app.addEmptyLabel("empty_1_0", column=1, row=0)
        app.addAutoEntry("auto_entry", words=file_content, column=0, row=3)
        app.setAutoEntryNumRows("auto_entry", 5)
        app.stopTab()

        app.startTab("User vs. Program")
        app.addLabel("l2", "Tab 2 Label")
        app.stopTab()

        app.stopTabbedFrame()

    app.go()
