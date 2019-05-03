import psutil
import sys

class getRes():
    @staticmethod
    def print_cpu():
        for name, value in psutil.cpu_times()._asdict().items():
            print("system.cpu." + str(name) + " " + str(value))

    @staticmethod
    def print_mem():
        for name, value in psutil.virtual_memory()._asdict().items():
            print("virtual " + str(name) + " " + str(value))

        for name, value in psutil.swap_memory()._asdict().items():
            print("swap " + str(name) + " " + str(value))

class help():
    @staticmethod
    def print_full_help():
        HELP="The script " + str(sys.argv[0]) + " provides in response cpu or memory resource utilization.\n\
        \n\
            Usage: " + str(sys.argv[0]) +" [cpu|mem]\n\
        \n\
            Where:\n\
            - cpu - prints CPU metrics\n\
            - mem - prints RAM metrics\n"

        print(HELP)

    @staticmethod
    def print_param_limit_exc(parameters,param_limit=1):

        print("To the script were provided such parameters: " + str(parameters))

        print("The script should accept only "+str(param_limit)+" parameter(s) to specify which metrics set to print:\n\
         - cpu - prints CPU metrics\n\
         - mem - prints RAM metrics\n")


if __name__=='__main__':
    PARAMETERS_LIMIT = 1

    if len(sys.argv) > PARAMETERS_LIMIT + 1:
        help.print_param_limit_exc(sys.argv,PARAMETERS_LIMIT)

    elif len(sys.argv) == 0:
        print("No input parameters identifed")
        help.print_full_help()

    else:
        for param in sys.argv[1:]:
            if param.lower()=="cpu":
                getRes.print_cpu()
            elif param.lower()=="mem":
                getRes.print_mem()
            else:
                print("Sorry, " + str(param) + " option not recognized.")
                help.print_full_help()
                exit(1)
