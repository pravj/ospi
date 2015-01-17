###How to use it

* In the `/config/config.json` add a GitHub Token from [Authorised Applications](https://github.com/settings/applications#personal-access-tokens).
* Required `scope` for the token is `public_repo` only.
* Running `/collector/main.py` will download all the data in `data` directory.
* `Rstudio` can be used for generating plots.
* A variable named `gplot` is used for all source files in the `/R` directory.
* Running `/classifier/main.py` will generate two `.txt` files in the `/results` directory.
  * One for `frequency` based and another for `probability` based sorted topic lists.
