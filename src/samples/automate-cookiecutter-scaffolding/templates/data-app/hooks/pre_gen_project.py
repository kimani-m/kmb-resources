import sys

def main():
    print("RUNNING PRE GENERATION...")
    validate('created_by', '{{ cookiecutter.created_by }}')
    validate('version', '{{ cookiecutter.version }}')
    return 0

def validate(cc_key, cc_value):
    
    if not cc_value.strip():
        print(f"ERROR(1): You failed to specify '{cc_key}'")
        sys.exit(1)
    return 0

if __name__ == '__main__':
    sys.exit(main())