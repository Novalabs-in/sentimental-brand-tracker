import pytest
import main

def test_brandsentimenttracker_instantiation():
    # Verify that the class BrandSentimentTracker is inspectable and loadable
    assert hasattr(main, 'BrandSentimentTracker')

