openapi: clean
	openapi-generator generate -i ../lib/openapi_3.1.json -g python -o generated/ \
	--global-property apiTests=false,apiDocs=false,modelTests=false,modelDocs=false,supportingFiles \
	--global-property models="JobHistoryResponseItem:JobHistoryResponse:JobState",apis="Jobs"

add_generated: openapi_gen
	uv add ./generated/

clean:
	rm -Rf ./generated/
