import subprocess


class CommandExecutionException(Exception):
    pass


def execute_command(command):

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = process.communicate()
    p_status = process.wait()

    if p_status != 0:

        error_message = "Something went wrong with your command: {}.".format(command)
        raise CommandExecutionException(error_message)

    return output
