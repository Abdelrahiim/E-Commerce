pytest_plugins = [
    "ecommerce.tests.selenium",
    "ecommerce.tests.fixtures",
    "ecommerce.tests.factories",
    "ecommerce.tests.api_client",
    "ecommerce.tests.promotion_fixtures",
    "celery.contrib.pytest",
]
