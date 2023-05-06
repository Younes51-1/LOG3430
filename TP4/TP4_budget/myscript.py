import os
os.system('git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect run python manage.py test')
