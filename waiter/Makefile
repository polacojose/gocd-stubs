add_generated: openapi
	uv add --editable ./generated/

openapi: clean
	openapi-generator generate -i ../lib/openapi.json -g python -o generated/ \
	--package-name gocd \
	--global-property apiTests=false,apiDocs=false,modelTests=false,modelDocs=false,supportingFiles \
	--global-property models="JobItem:JobHistory:JobState:JobStateTransition",apis="Jobs"

clean:
	rm -Rf ./generated/
