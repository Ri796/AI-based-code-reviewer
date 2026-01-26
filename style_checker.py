import autopep8

def show_style_corrected(code):
    try:
        corrected_code = autopep8.fix_code(code)
        return {
            "success": True,
            "corrected_code": corrected_code
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
