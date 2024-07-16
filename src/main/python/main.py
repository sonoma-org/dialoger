from app import App
import click
import logging

@click.command()
@click.option('--debug', default=False, help='Debug True/False')
def main(debug):

    file_log = logging.FileHandler("dialoger-auth.log")
    console_out = logging.StreamHandler()

    if debug == True:
        logging.basicConfig(level=logging.DEBUG,
        handlers=(file_log, console_out),
        format="%(asctime)s %(levelname)s %(message)s")
    else:
        logging.basicConfig(level=logging.INFO,
        handlers=(file_log, console_out),
        format="%(asctime)s %(levelname)s %(message)s")

    Server = App()
    Server.init()


if __name__ == '__main__':
    main()