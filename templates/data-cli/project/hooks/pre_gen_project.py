import sys, click, time, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.INFO("Running pre-gen checks.")
    #TODO: Create a loop against a list of inputs to validate
    validate('created_by', '{{ cookiecutter.created_by }}')
    validate('version', '{{ cookiecutter.version }}')
    if {{ cookiecutter.debug_run }}:            
        with click.progressbar(length=10, label="Processing", show_eta=False) as progress_bar:  
            logger.DEBUG(" Validating 'created_by' input.")
            progress_bar.update(50)
            time.sleep(1.00)
            logger.DEBUG(" Validating 'version' input.")
            progress_bar.update(50)
            time.sleep(1.00)
    logger.INFO("Completed pre-gen checks.")
    return 0

def validate(cc_key, cc_value):    
    if not cc_value.strip():
        logger.ERROR(f"ERROR(1): You failed to specify '{cc_key}'")
        sys.exit(1)
    return 0

if __name__ == '__main__':
    sys.exit(main())