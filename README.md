# **ReadMe ApiJanuaryProject**
## Mathieu Du Jardin 2IoT
* ### gekozen thema
  > Ik heb een API rond auto's geschreven. Mij leek het interessant om hierond een API rond te schrijven omdat ik van auto's hou en omdat dit ook in de praktijk gebruikt kan worden (niet mijn API, deze zou dan professioneler en beter moeten zijn).
  >
  > Mijn 1e GET request zorgt ervoor dat er X aantal auto's worden weergegeven.<br />
  > Mijn 2e GET request is eigenlijk niet zo heel belangrijk maar stel dat je geen X aantal auto's ingeeft dan krijg je standaard 5 auto's. Ik heb hiervoor een 2e get request gemaakt omdat ik dit beter vond dan een default waarde van 5 te stoppen in de eerste want dan moest je andere dingen met het path doen.<br />
  > Mijn 3e GET request laat je auto's selecteren op basis van een kleur (rood, blauw...)<br />
  > Mijn 4e GET request laat je auto's selecteren op basis van een minimum en maximum horsepower die je wilt.<br />
  > Ik heb ook een POST request waarmee je auto's kan toevoegen.<br />
  > Met mijn DELETE request kan je een auto op basis van merk verwijderen.<br />
  > Met mijn PUT request kan je een auto zijn horsepower aanpassen.<br />
  > 
  > Ik heb voor de database, hashing en OAuth twee GET requests toegevoegd en 1 POST request. Met de eerste GET request kan je de lijst met users terug vinden, met de 2e get request kan je een user op basis van ID terugvinden. Met de POST request kan je een user aanmaken. Deze 3 requests bevatten OAuth, hashing en werken met een database. <br />
  > 
  > Als laatste is er nog 1 POST request voor de token. <br />
* ### uitbreiding
  >Test alle GET endpoints van een van je APIs via de Requests en pytest library (+10%) <br />
  >Test alle niet-GET endpoint (+10%) <br />
  >Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat (+15%) <br />
  >Host de front-end op netlify (+10%) <br />
  >Geef de front-end een leuke stijlgeving (+10%) <br />
 
* ### links
  * #### hosted API op Oketo
    * [Oketo endpoint](https://system-service-mathieudj.cloud.okteto.net)
  * #### GitHub repo
    * [repo](https://github.com/MathieuDJ/ApiJanuaryProject.git)
  * #### link hosted front-end Netlify
    * [netlify front-end](https://transcendent-syrniki-fe2fcd.netlify.app)

* ### Screenshot OpenAPI-docs
![Image api docs](https://user-images.githubusercontent.com/72858870/211358282-d19f247c-a3f2-46f9-a841-e89819f684a0.png)
* ### Postman screenshots
  * #### GET X aantal auto's
  ![GET](https://user-images.githubusercontent.com/72858870/211359116-4fc0b9fa-6d94-477b-9479-fd46e75b9d21.png)
  * #### GET zonder X aantal auto's geeft er altijd 5 terug
  ![GET](https://user-images.githubusercontent.com/72858870/211359354-544b013e-ef8f-4f38-8edc-6ccf6ec92f24.png)
  * #### GET auto met bepaalde kleur
  ![GET](https://user-images.githubusercontent.com/72858870/211359566-0a604fe3-4c7b-4e43-b6aa-0c21051634ac.png)
  * ### GET auto met min X en max X horsepower
  ![GET](https://user-images.githubusercontent.com/72858870/211359693-5ee0e6d6-91b3-4711-bc01-c00cfe9dc98d.png)
  * ### POST een auto
  ![GET](https://user-images.githubusercontent.com/72858870/211359939-2cb88b82-fa0e-4da4-8d0e-118cf9938c95.png)
  * ### DELETE een auto met een bepaald merk
  ![GET](https://user-images.githubusercontent.com/72858870/211360173-ed68ab9e-b7ea-44ca-885d-0ce2250e6634.png)
  * ### PUT update een auto zijn horsepower
  ![GET](https://user-images.githubusercontent.com/72858870/211361595-6a591105-0c12-4da2-9075-f00d2bf9e11b.png)
  * ### POST een user
  ![GET](https://user-images.githubusercontent.com/72858870/211361856-fa3f5df6-b564-4d79-856f-cb6efa718b91.png)
  * ### GET users
  ![GET](https://user-images.githubusercontent.com/72858870/211361970-fabe6d83-1eb5-4cc4-80d0-d62830b1d67b.png)
  * ### POST user door een ID
  ![GET](https://user-images.githubusercontent.com/72858870/211362051-e8f64c3f-06ca-461d-8bc2-84018bbd8abd.png)
