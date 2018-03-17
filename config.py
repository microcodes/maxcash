class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = False
	TESTING = False


class DevelopmentConfig(Config):
	SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
	pass


class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
	SQLALCHEMY_ECHO = True
	TESTING = True


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}