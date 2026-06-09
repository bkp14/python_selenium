import logging

def log_creator():
    logging.basicConfig(
        filename="testlogreport.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True
    )

    return logging.getLogger()