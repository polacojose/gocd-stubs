build:
	uv export --no-dev --no-hashes -o requirements.txt
	uv export --dev --no-hashes -o dev-requirements.txt
	podman build -t retreat-cart .

run: build
	podman run --rm -p 8000:8000 retreat-cart

openapi:
	python3 genopenapi.py
	#openapi_downgrade openapi_3.1.json openapi.json
