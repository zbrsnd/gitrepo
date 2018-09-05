<h1>PIERWSZA STRONA PHP</h1>

<?php
                  //  phpinfo()
  print_r($_POST); //tablica w ktorej wyswietlane sa wszystkie wartosci GET z formluarza
  ?>

<form name="formularz" id="formularz" method="POST">
  <table class="table">

    <tr>
      <td><label for="imie">Imię:</label></td>
      <td><input type="text" name="imie" value=""></td>
    </tr>

    <tr>
      <td><label for="naziwsko">Nazwisko:</label></td>
      <td><input type="text" name="nazwisko" value=""></td>
    </tr>
</table>

  <input type="submit" name="" value="Prześlij">
  <input type="reset" name="" value="Resetuj">

<fieldset>
<legend>Wybierz płeć</legend>
  <input type="radio" name="gender" value="m" checked> Mężczyzna<br>
  <input type="radio" name="gender" value="f"> Kobieta<br>
  <input type="radio" name="gender" value="a"> Alien<br>
  <input type="radio" name="gender" value="o"> Inna
</fieldset>

<fieldset>
<legend>Wybierz pojazd</legend>
<input type="checkbox" name="vehicle1" value="Bike"> Rower<br>
<input type="checkbox" name="vehicle2" value="Car"> Samochód
</fieldset>

<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab" selected>Saab</option>
<option value="fiat">Fiat</option>

<option value="audi">Audi</option>
</select>
<select name="cars2" multiple>
<option value="volvo">Volvo</option>
<option value="saab" selected>Saab</option>
<option value="fiat">Fiat</option>
<option value="audi">Audi</option>
</select>

<br>
<textarea name="message" rows="10" cols="30">Wyżal się!</textarea>
<br>
</form>
