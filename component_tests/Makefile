add_generated: openapi
	uv add ./generated/

openapi: clean
	openapi-generator generate -i ../lib/openapi.json -g python -o generated/ \
	--package-name gocd \
	--global-property apiTests=false,apiDocs=false,modelTests=false,modelDocs=false

clean:
	rm -Rf ./generated/
