run:
	@uvicorn store.main:app --reload

create-migrations:
	@alembic revision --autogenerate -m d=init_db

run-migrations:
	@alembic upgrade head

save-libs:
	@pip freeze > requirements.txt

test:
    @pytest tests