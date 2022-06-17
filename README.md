<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <h1>Starwars api with FastApi</h1>
</div>


## About The Project

The project uses clean code principles with compose design patterns to create API to consume StarWars API.

## Built With

* Python3
* FastApi
* Requests
* Pytest
* Pre-commit
* Pylint
* Flake8
* Black

## Row to run and contribute

1. Use virtual env to install and run this project
    ```sh
    python3 -m venv venv && source venv/bin/activate
    ```
2. Install requiriments
   ```sh
   pip3 install -r requirements.txt
   ```
3. Run the dev server
   ```sh
   python3 run.py
   ```
4. When you commit, pre-commit runs and make some verifications and freeze requiriments.txt. To update and add new configs, open `.pre-commit-config.yaml`.

## Commit pattern

We use the conventional Commits, you can see more details in the [documentation](https://www.conventionalcommits.org/en/v1.0.0/)

Example: type: description


## Roadmap

- [x] Add Fast Api
- [ ] Add alchemySql
- [ ] Configure alchemySql with Postgres and MongoDb
- [ ] CRUD with starships

# Thanks

Special thanks to [Rafael Ferreira](https://www.linkedin.com/in/rafael-ferreira-760405167/), for sharing your knowledge and making learning a happy moment. Thank you!


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/filipenmarques1
