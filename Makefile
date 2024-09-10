# My IDE automatically converts tabs to spaces
.RECIPEPREFIX = +

.PHONY: deploy

deploy:
+ gcloud app deploy app.yaml --project spring-street-island --promote

