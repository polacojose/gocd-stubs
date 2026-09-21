add_generated: openapi
	uv add --editable ./generated/

openapi: clean
	openapi-generator generate -i ../lib/openapi_3.1.json -g python -o generated/ \
	--api-package gocd \
	--package-name gocd \
	--global-property apiTests=false,apiDocs=false,modelTests=false,modelDocs=false,supportingFiles \
	--global-property models="JobItem:JobHistoryResponse:JobState:JobStateTransition",apis="Jobs"

clean:
	rm -Rf ./generated/
