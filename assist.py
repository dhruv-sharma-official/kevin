import main_engine

if __name__ == "__main__": ## program execution starts from here ###################################################################
    # main_engine.onStart()
    while True:
        main_engine.hardware_control.btrycheck()
        user = main_engine.takecmd()
        main_engine.recognize(user)
        

