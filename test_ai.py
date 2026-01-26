try:
    from ai_suggester import get_code_suggestions
    print("✅ Import successful")
    # We won't call the AI to save tokens/time, just checking imports & function existence
    if callable(get_code_suggestions):
        print("✅ Function found")
except ImportError as e:
    print(f"❌ Import failed: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
