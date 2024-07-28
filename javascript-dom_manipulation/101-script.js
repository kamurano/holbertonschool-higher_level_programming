// Script that fetches and prints hello depending on the language

const languageCode = document.getElementById('language_code');
const btnTranslate = document.getElementById('btn_translate');
const helloElement = document.getElementById('hello');

btnTranslate.onclick = () => {
  const selectedLanguage = languageCode?.value || "en";

  let url = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;

  fetch(url)
    .then(res => {
      if (!res.ok) throw new Error(res.status);
      return res.json();
    })
    .then(data => {
      if (data?.hello) {
        helloElement.innerHTML = data.hello;
      } else {
        helloElement.innerHTML = `Translation not found`;
      }
    });
};