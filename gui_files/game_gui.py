from appJar import gui as gui
import file_handler as fh

file_content = fh.file_reader(read_file="words.txt", encoding='ISO-8859-1')


def ordspel_gui():
    with gui("Ordspelet") as app:

        # BODY SETTINGS
        app.setSize(300, 400)
        app.setLocation(0, 200)

        # Y GROUPS (used for mass controlling column groups)
        y_group0 = 0
        y_group1 = 1
        y_group2 = 2
        y_group3 = 3

        # X GROUPS (used for mass controlling row groups)
        x_group0 = 0
        x_group1 = 1
        x_group2 = 2
        x_group3 = 3
        x_group4 = 4
        x_group5 = 5

        # ///// START TABBED FRAMES \\\\\
        app.startTabbedFrame("TabbedFrame")
        app.setTabbedFrameTabExpand("TabbedFrame", expand=True)

        # ------------------------------------- NEW TAB -------------------------------------

        # TAB NAME
        app.startTab("Program vs. User")

        app.addLabel("ti_pro_usr", f"saker med grejer", column=0, row=0)
        app.addEmptyLabel("empty_1_0", column=1, row=0)
        app.addAutoEntry("auto_entry", words=file_content, column=0, row=3)
        app.setAutoEntryNumRows("auto_entry", 5)

        app.stopTab()

        # ------------------------------------- STOP TAB -------------------------------------

        # ------------------------------------- NEW TAB -------------------------------------

        # TAB NAME
        app.startTab("User vs. Program")

        # LABEL COUNTER
        app.label_counter = 1

        def label_picker():

            if app.label_counter == 1:
                app.label_counter += 1
                return 1
            elif app.label_counter == 2:
                app.label_counter += 1
                return 2
            elif app.label_counter == 3:
                app.label_counter += 1
                return 3
            elif app.label_counter == 4:
                app.label_counter = 1
                return 4

        # TAB FUNCTIONS
        def press(value):
            if value == "SUBMIT":
                # USES Y GROUP 3
                app.setLabelChan(f"3_EL{label_picker()}", f"{int(app.getEntry('clue'))}")

        # Y GROUP 0
        app.addEmptyLabel("0_EL0", column=y_group0, row=x_group0)
        app.addEmptyLabel("0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("0_EL3", column=y_group0, row=x_group3)

        # Y GROUP 1 // WORD GUESS HERE AND USER INPUT HERE
        app.addEmptyLabel("1_EL0", column=y_group1, row=x_group0)
        app.addLabel("1_L1", f"{app.label_counter}", column=y_group1, row=x_group1)
        app.addNumericEntry("clue", column=y_group1, row=x_group2)
        app.addButton("SUBMIT", press, column=y_group1, row=x_group3)

        # Y GROUP 2
        app.addEmptyLabel("2_EL1", column=y_group2, row=x_group0)

        # Y GROUP 3 // WORD GUESS HISTORY HERE ; ONLY 4 CONTENT SLOTS
        app.addLabel("3_EL0", column=y_group3, row=x_group0)
        app.addEmptyLabel("3_EL1", column=y_group3, row=x_group1)
        app.addEmptyLabel("3_EL2", column=y_group3, row=x_group2)
        app.addEmptyLabel("3_EL3", column=y_group3, row=x_group3)
        app.addEmptyLabel("3_EL4", column=y_group3, row=x_group4)

        app.stopTab()

        # ------------------------------------- STOP TAB -------------------------------------

        # \\\\\ STOP TABBED FRAMES /////
        app.stopTabbedFrame()

    # RUNS GUI APPLICATION
    app.go()


ordspel_gui()
