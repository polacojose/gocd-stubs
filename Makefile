GOCD_VERSION=`toml2json lib/pyproject.toml | jq '.project."gocd-version"' | tr -d '"'`

openapi: clean

	( cd lib && \
		source .venv/bin/activate && \
		make openapi)

	( cd tests && \
		source .venv/bin/activate && \
		make openapi && \
		pytest ./tests/ -v)

	mkdir -p build
	cp lib/openapi.json build/gocdapi-$(GOCD_VERSION).json

clean: 
	rm -Rf build || true
	rm lib/openapi.json || true
