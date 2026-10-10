GOCD_VERSION=`grep -r gocd-version lib/pyproject.toml | awk '{print $$3}' | tr -d '"'`

build/gocdapi.json: lib/openapi.json
	( cd tests && \
		make generated && \
		uv venv && \
		uv sync && \
		. .venv/bin/activate && \
		pytest ./tests/ -v)

	mkdir -p build
	cp lib/openapi.json build/gocdapi.json
	cp lib/openapi.json build/gocdapi-$(GOCD_VERSION).json

lib/openapi.json:
	( cd lib && \
		uv venv && \
		uv sync && \
		. .venv/bin/activate && \
		make openapi.json)

clean: 
	( cd tests && \
		make clean)
	( cd lib && \
		make clean)
	rm -Rf build
	rm -f lib/openapi.json
	rm -Rf tests/generated
