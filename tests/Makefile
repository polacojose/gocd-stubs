generated:
	openapi-generator-cli generate -i ../lib/openapi.json -g python \
	--package-name gocd \
	--global-property apiTests=false,apiDocs=false,modelTests=false,modelDocs=false \
	-o generated/

clean:
	rm -Rf ./generated/
